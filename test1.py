import wiringpi
import sys
import argparse

def process_command(command):
    cmd = command[0:3]  # Получаем команду cmd

    if cmd[0:1] == 'LG':
        channel = int(command[2])
        state = int(command[5])    
        process_LG_command(channel, state)
    elif cmd[0] == 'L':
        channel = int(command[1])
        state = int(command[3])
        process_L_command(channel, state)
    elif cmd[0:1] == 'LR':
        channel = int(command[2])
        state = int(command[5])
        process_LR_command(channel, state)
    elif cmd == 'B':
        channel = int(command[1])
        state = int(command[3])
        process_B_command(channel, state)
    elif cmd == 'REL':
        channel = int(command[3])
        state = int(command[5])        
        process_REL_command(channel, state)
    else:
        print(f"Error: Invalid command {cmd}")



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
            if char == ord('\n'):  # Обрабатываем сообщение при достижении длины 5 или при символе новой строки
                process_command(message)
                wiringpi.serialPuts(serial, "OK\n")  # Отправляем "OK" обратно в порт
                message = ""  # Очищаем сообщение для следующей итерации
            else:
                message += chr(char)  # Добавляем символ к полученному сообщению
except KeyboardInterrupt:
    print("\nexit")
    sys.exit(0)

wiringpi.serialClose(serial)  # Закрываем соединение по UART
