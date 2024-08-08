import serial
import time

# Configuração da porta serial
port = '/dev/ttyACM0'  # Substituir com a sua porta serial
                       # Utilize 'ls -la /dev/ttyACM*' para identificar
baudrate = 115200
timeout = 1  # segundos

# Abrir a porta serial
ser = serial.Serial(port, baudrate, timeout=timeout)

def read_serial_data():
    while True:
        try:
            # Leia uma linha da porta serial
            line = ser.readline().decode('utf-8').strip()
            if line:
                # Divida a linha em accX, accY, accZ
                tuple_string = line.split(',')
                if len(tuple_string)!= 3 :
                    print("Formato de dados inválido!")
                else:
                    accX, accY, accZ = float(tuple_string[0]),float(tuple_string[1]),float(tuple_string[2]) 
                    # Imprimir os dados
                    print(f"{accX},{accY},{accZ}")
                # Adicione um pequeno atraso para corresponder à taxa de dados (63Hz)
                time.sleep(1/63)
        except Exception as e:
            print(f"Error: {e}")
            break

if __name__ == "__main__":
    try:
        read_serial_data()
    except KeyboardInterrupt:
        print("Parando o script.")
    finally:
        ser.close()
