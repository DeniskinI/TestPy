import wiringpi
import sys
import argparse

parser = argparse.ArgumentParser(description='')
parser.add_argument("--device", type=str, default="/dev/ttyS3", help='specify the serial node')
args = parser.parse_args()

wiringpi.wiringPiSetup()
serial = wiringpi.serialOpen(args.device, 115200)
if serial < 0:
    print("Unable to open serial device: %s"% args.device)
    sys.exit(-1)


message = ""  # Переменная для хранения полученных символов

try:
    while True:
        if wiringpi.serialDataAvail(serial):  # Проверяем наличие данных в UART
            char = wiringpi.serialGetchar(serial)  # Читаем символ из UART
            if char == ord('\n'):  # Проверяем, является ли символ символом новой строки
                if message.startswith('LG'):  # Проверяем, начинается ли сообщение с 'LG'
                    channel = int(message[2])  # Получаем номер канала
                    state = int(message[4])  # Получаем состояние канала
                    print(f"Received command: Channel {channel}, State {state}")
                message = ""  # Очищаем сообщение для следующей итерации
            else:
                message += chr(char)  # Добавляем символ к полученному сообщению
except KeyboardInterrupt:
    print("\nexit")
    sys.exit(0)

wiringpi.serialClose(serial)  # Закрываем соединение по UART
