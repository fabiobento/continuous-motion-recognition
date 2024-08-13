import serial
import time
import sys

WINDOW_SIZE = 125
STRIDE = 50  # 50  # Defina o passo(stride), ou seja, o número de amostras para avançar após cada classificação

# Configure sua porta serial aqui
ser = serial.Serial("/dev/ttyACM0", 115200, timeout=1)  # Ajuste conforme necessário


def read_serial_data():
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
                            print(window[: WINDOW_SIZE * 3])
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
    try:
        read_serial_data()
    except KeyboardInterrupt:
        print("Parando o script.")
    finally:
        ser.close()
