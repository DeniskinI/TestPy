import wiringpi
import sys
import argparse
from wiringpi import GPIO

def process_command(command):
    cmd = command[0:3]  # Получаем команду cmd
    
def process_command(command):
    cmd = command[0:3]  # Получаем команду cmd
    
    if cmd[0] == 'L':
        if cmd[1] == 'R':
            channel = int(command[2])
            state = int(command[4])
            process_LR_command(channel, state)      
        elif cmd[1] == 'G':
            channel = int(command[2])
            state = int(command[4])    
            process_LG_command(channel, state)       
        elif cmd[1].isdigit():
            channel = int(command[1])
            state = int(command[3])
            process_L_command(channel, state)        
        else:
            print(f"Error: Invalid command {cmd}")
    elif cmd[0] == 'B':
        channel = int(command[1])
        state = int(command[3])
        process_B_command(channel, state)
    elif cmd[0:3] == 'REL':
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
    
wiringpi.wiringPiSetup()

wiringpi.pinMode(20, GPIO.OUTPUT)
wiringpi.pinMode(13, GPIO.OUTPUT)
wiringpi.pinMode(4, GPIO.OUTPUT)
wiringpi.pinMode(3, GPIO.OUTPUT)

wiringpi.pinMode(25, GPIO.OUTPUT)
wiringpi.pinMode(12, GPIO.OUTPUT)
wiringpi.pinMode(2, GPIO.OUTPUT)
wiringpi.pinMode(0, GPIO.OUTPUT)

wiringpi.pinMode(9, GPIO.OUTPUT)
wiringpi.pinMode(11, GPIO.OUTPUT)
wiringpi.pinMode(26, GPIO.OUTPUT)
wiringpi.pinMode(23, GPIO.OUTPUT)

wiringpi.pinMode(7, GPIO.OUTPUT)
wiringpi.pinMode(10, GPIO.OUTPUT)
wiringpi.pinMode(16, GPIO.OUTPUT)
wiringpi.pinMode(22, GPIO.OUTPUT)

wiringpi.pinMode(5, GPIO.OUTPUT)
wiringpi.pinMode(8, GPIO.OUTPUT)
wiringpi.pinMode(14, GPIO.OUTPUT)
wiringpi.pinMode(21, GPIO.OUTPUT)

wiringpi.pinMode(24, GPIO.OUTPUT)


wiringpi.pinMode(19, GPIO.INPUT)
wiringpi.pinMode(15, GPIO.INPUT)
wiringpi.pinMode(6, GPIO.INPUT)
wiringpi.pinMode(1, GPIO.INPUT)


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
