import wiringpi
import sys
import argparse
from wiringpi import GPIO

def process_command(command):
    cmd = command[0:3]  # Получаем команду cmd
    
def process_command(command):
    retval = True
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
            retval = False
    elif cmd[0] == 'B':
        channel = int(command[1])
        state = int(command[3])
        process_B_command(channel, state)
    elif cmd[0:3] == 'REL':
        channel = int(command[3])
        state = int(command[5])        
        process_REL_command(channel, state)
    elif cmd[0] == 'S':
        channel = int(command[1])
        process_S_command(channel)
    else:
        print(f"Error: Invalid command {cmd}")
        retval = False
        
    return retval


def process_S_command(channel):
    # Обработка команды S
    print(f"Processing S command: Channel {channel}")
    
    if channel == 1:
        level =  wiringpi.digitalRead(19)
        print(f"Level: {level}")
    elif channel == 2:
        level =  wiringpi.digitalRead(15)
        print(f"Level: {level}")
    elif channel == 3:
        level =  wiringpi.digitalRead(6)
        print(f"Level: {level}")
    elif channel == 4:
        level =  wiringpi.digitalRead(1)
        print(f"Level: {level}")
    else:
        print(f"Error: Invalid parametr channel {channel}")

def process_LG_command(channel, state):
    # Обработка команды LG
    print(f"Processing LG command: Channel {channel}, State {state}")
    if channel == 1:
        if state == 0:
            wiringpi.digitalWrite(7, GPIO.LOW)
        else:
            wiringpi.digitalWrite(7, GPIO.HIGH)
    
    elif channel == 2:
        if state == 0:
            wiringpi.digitalWrite(10, GPIO.LOW)
        else:
            wiringpi.digitalWrite(10, GPIO.HIGH)
    
    elif channel == 3:
        if state == 0:
            wiringpi.digitalWrite(16, GPIO.LOW)
        else:
            wiringpi.digitalWrite(16, GPIO.HIGH)
    
    
    elif channel == 4:
        if state == 0:
            wiringpi.digitalWrite(22, GPIO.LOW)
        else:
            wiringpi.digitalWrite(22, GPIO.HIGH)
    
    
    else:
        print(f"Error: Invalid parametr channel {channel}")


def process_L_command(channel, state):
    # Обработка команды L
    print(f"Processing L command: Channel {channel}, State {state}")
    
    if channel == 1:
        if state == 0:
            wiringpi.digitalWrite(25, GPIO.LOW)
        else:
            wiringpi.digitalWrite(25, GPIO.HIGH)
    
    elif channel == 2:
        if state == 0:
            wiringpi.digitalWrite(12, GPIO.LOW)
        else:
            wiringpi.digitalWrite(12, GPIO.HIGH)
    
    elif channel == 3:
        if state == 0:
            wiringpi.digitalWrite(2, GPIO.LOW)
        else:
            wiringpi.digitalWrite(2, GPIO.HIGH)
    
    
    elif channel == 4:
        if state == 0:
            wiringpi.digitalWrite(0, GPIO.LOW)
        else:
            wiringpi.digitalWrite(0, GPIO.HIGH)
    
    
    else:
        print(f"Error: Invalid parametr channel {channel}")    

def process_LR_command(channel, state):
    # Обработка команды LR
    print(f"Processing LR command: Channel {channel}, State {state}")
    
    if channel == 1:
        if state == 0:
            wiringpi.digitalWrite(9, GPIO.LOW)
        else:
            wiringpi.digitalWrite(9, GPIO.HIGH)
    
    elif channel == 2:
        if state == 0:
            wiringpi.digitalWrite(11, GPIO.LOW)
        else:
            wiringpi.digitalWrite(11, GPIO.HIGH)
    
    elif channel == 3:
        if state == 0:
            wiringpi.digitalWrite(26, GPIO.LOW)
        else:
            wiringpi.digitalWrite(26, GPIO.HIGH)
    
    
    elif channel == 4:
        if state == 0:
            wiringpi.digitalWrite(23, GPIO.LOW)
        else:
            wiringpi.digitalWrite(23, GPIO.HIGH)
    
    
    else:
        print(f"Error: Invalid parametr channel {channel}")    

def process_B_command(channel, state):
    # Обработка команды B
    print(f"Processing B command: Channel {channel}, State {state}")
    
    if channel == 1:
        if state == 0:
            wiringpi.digitalWrite(5, GPIO.LOW)
        else:
            wiringpi.digitalWrite(5, GPIO.HIGH)
    
    elif channel == 2:
        if state == 0:
            wiringpi.digitalWrite(8, GPIO.LOW)
        else:
            wiringpi.digitalWrite(8, GPIO.HIGH)
    
    elif channel == 3:
        if state == 0:
            wiringpi.digitalWrite(14, GPIO.LOW)
        else:
            wiringpi.digitalWrite(14, GPIO.HIGH)
    
    
    elif channel == 4:
        if state == 0:
            wiringpi.digitalWrite(21, GPIO.LOW)
        else:
            wiringpi.digitalWrite(21, GPIO.HIGH)
    
    
    else:
        print(f"Error: Invalid parametr channel {channel}")    

def process_REL_command(channel, state):
    # Обработка команды REL
    print(f"Processing REL command: Channel {channel}, State {state}")
    
    if channel == 1:
        if state == 0:
            wiringpi.digitalWrite(20, GPIO.LOW)
        else:
            wiringpi.digitalWrite(20, GPIO.HIGH)
    
    elif channel == 2:
        if state == 0:
            wiringpi.digitalWrite(13, GPIO.LOW)
        else:
            wiringpi.digitalWrite(13, GPIO.HIGH)
    
    elif channel == 3:
        if state == 0:
            wiringpi.digitalWrite(4, GPIO.LOW)
        else:
            wiringpi.digitalWrite(4, GPIO.HIGH)
    
    
    elif channel == 4:
        if state == 0:
            wiringpi.digitalWrite(3, GPIO.LOW)
        else:
            wiringpi.digitalWrite(3, GPIO.HIGH)
    
    
    else:
        print(f"Error: Invalid parametr channel {channel}")    

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
            if char == ord('\n'):  # Обрабатываем сообщение при символе новой строки
                wiringpi.digitalWrite(24, GPIO.HIGH)
                wiringpi.delayMicroseconds(50000)
                
                if process_command(message) == True:
                    wiringpi.serialPuts(serial, "OK\n")  # Отправляем "OK" обратно в порт
                else:
                    wiringpi.serialPuts(serial, "ERROR\n")
                message = ""  # Очищаем сообщение для следующей итерации
                
                wiringpi.digitalWrite(24, GPIO.LOW)
                wiringpi.delayMicroseconds(50000)
                
            else:
                message += chr(char)  # Добавляем символ к полученному сообщению
except KeyboardInterrupt:
    print("\nexit")
    sys.exit(0)

wiringpi.serialClose(serial)  # Закрываем соединение по UART
