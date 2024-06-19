import wiringpi
import sys
import argparse

def process_command(command):
    cmd = command[0:2]  # Получаем команду cmd
    channel = int(command[2])  # Получаем номер канала x
    state = int(command[4])  # Получаем состояние y

    if cmd == 'LG':
        process_LG_command(channel, state)
    elif cmd == 'L':
        process_L_command(channel, state)
    elif cmd == 'LR':
        process_LR_command(channel, state)
    elif cmd == 'B':
        process_B_command(channel, state)
    elif cmd == 'REL':
        process_REL_command(channel, state)
    else:
        print("Error: Invalid command")

def process_LG_command(channel, state):
    # Обработка команды LG
    print(f"Processing LG command: Channel {channel}, State {state}")

def process_L_command(channel, state):
    # Обработка команды L
    print(f"Processing L command: Channel {channel}, State {state}")

def process_LR_command(channel, state):
    # Обработка команды LR
    print(f"Processing LR command: Channel {channel}, State {state}")

def process_B_command(channel, state):
    # Обработка команды B
    print(f"Processing B command: Channel {channel}, State {state}")

def process_REL_command(channel, state):
    # Обработка команды REL
    print(f"Processing REL command: Channel {channel}, State {state}")

parser = argparse.ArgumentParser(description='')
parser.add_argument("--device", type=str, default="/dev/ttyS3", help='specify the serial node')
args = parser.parse_args()

wiringpi.wiringPiSetup()
serial = wiringpi.serialOpen(args.device, 115200)
if serial < 0:
    print("Unable to open serial device: %s" % args.device)
    sys.exit(-1)

message = ""  # Переменная для хранения полученных символов

try:
    while True:
        if wiringpi.serialDataAvail(serial):  # Проверяем наличие данных в UART
            char = wiringpi.serialGetchar(serial)  # Читаем символ из UART
            if char == ord('\n'):  # Проверяем, является ли символ символом новой строки
                if len(message) == 5:  # Проверяем, что длина сообщения равна 5 символам (формат "cmdx y")
                    process_command(message)
                    wiringpi.serialPuts(serial, "OK\n")  # Отправляем "OK" обратно в порт
                else:
                    print("Error: Invalid command format")
                    wiringpi.serialPuts(serial, "Error: Invalid command format\n")  # Отправляем ошибку обратно в порт
                message = ""  # Очищаем сообщение для следующей итерации
            else:
                message += chr(char)  # Добавляем символ к полученному сообщению
except KeyboardInterrupt:
    print("\nexit")
    sys.exit(0)

wiringpi.serialClose(serial)  # Закрываем соединение по UART
