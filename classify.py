# Referência:
#      https://docs.edgeimpulse.com/docs/tools/edge-impulse-for-linux/linux-python-sdk
#      https://docs.edgeimpulse.com/docs/edge-ai-hardware/cpu/linux-x86_64
# Ajuda:
#      - Primeiro baixe o impulso completo do edge impulse com a seguinte linha de comando:
#           $ edge-impulse-linux-runner --clean --download modelfile.eim
#      - Depois execute esse script:
#           $python3 classify.py ./model.eim
#

import serial
import time
import sys
from edge_impulse_linux.runner import ImpulseRunner

# Hiperparâmetros para leitura de dados em janela deslizante
WINDOW_SIZE = 125
STRIDE = 50  # 50  # Defina o passo(stride), ou seja, o número de amostras para avançar após cada classificação

# Configuração da porta serial
port = "/dev/ttyUSB0"  # Substituir com a sua porta serial
# Para identificar a porta serial utilize:
#    ls -la /dev/ttyACM*
#    ls -la /dev/ttyUSB*
baudrate = 115200
timeout = 1  # segundos

# Abrir a porta serial
ser = serial.Serial(port, baudrate, timeout=timeout)


def classify_data(features, runner):
    res = runner.classify(features)
    print("classificação:")
    print(res["result"])
    print("tempo:")
    print(res["timing"])


def read_serial_data(runner):
    window = []
    try:
        while True:
            line = ser.readline().decode("utf-8").strip()
            if line:
                tuple_string = line.split(",")
                if len(tuple_string) != 3:
                    print("Formato de dados inválido!")
                else:
                    try:
                        accX, accY, accZ = (
                            float(tuple_string[0]),
                            float(tuple_string[1]),
                            float(tuple_string[2]),
                        )
                        window.extend([accX, accY, accZ])
                        if len(window) >= WINDOW_SIZE * 3:
                            classify_data(window[: WINDOW_SIZE * 3], runner)
                            # Retenção de parte da janela com base no stride
                            window = window[
                                STRIDE * 3 :
                            ]  # Keep the last `STRIDE` data points
                    except ValueError as e:
                        print(f"Erro de conversão: {e} para a linha '{line}'")
                        continue  # Ignora a linha se a conversão falhar
                time.sleep(1 / 63)  # Manter a taxa de amostragem de dados
    except Exception as e:
        print(f"Error: {e}")
    finally:
        ser.close()


if __name__ == "__main__":
    model = (
        sys.argv[1]
        if len(sys.argv) > 1
        else "/home/fabio/Documentos/vscode/continuous-motion-recognition/modelfile.eim"
    )
    runner = ImpulseRunner(model)
    try:
        model_info = runner.init()
        print(
            'Carregado o runner para "'
            + model_info["project"]["owner"]
            + " / "
            + model_info["project"]["name"]
            + '"'
        )
        read_serial_data(runner)
    finally:
        if runner:
            runner.stop()
