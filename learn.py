import serial
import time


serial.Serial()

ser=serial.Serial(
port='COM10',
baudrate=9600,
timeout = 0,
)

a = 0

def SVM():
    if a > 13:
        return 1
    else:
        return 0


def ork():
    code = []
    data1 = "0"
    data2 = "0"
    data3 = "0"

    time.sleep(0.2)
    serialline = ser.readline()
    s = ''
    for a in serialline:
        s += chr(a)
    code = s.split(',')
    if s:
        data1 = code[0]
        data2 = code[1]
        data3 = code[2]
        print(data1)
        print(' ')
        print(data2)
        print(' ')
        print(data3)
        if data3!='':
            a = int(data3)
        print(a)

i = 0
print('start')
while 1:
    if ser.read(5):
        break

while i < 200:
    try:
        ork()
        i = i + 1
    except KeyboardInterrupt:
        break
print('Authorizating completed')
if SVM()==1:
    print('Logined succesfully!')
else:
    print('Permission denied')
ser.close()



