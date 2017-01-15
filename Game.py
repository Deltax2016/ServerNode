import serial
import time


serial.Serial()

ser=serial.Serial(
port='COM11',
baudrate=9600,
timeout = 0,
)

f1 = open('data6.log', "a")

#def ork():
  #  code = []
   # data1 = "0"
  #  data2 = "0"
 #   data3 = "0"

 #   time.sleep(0.2)
 #   serialline = ser.readline()
#    s = ''
#    for a in serialline:
#        s += chr(a)
#    code = s.split(',')
#    if s:
 #       data1 = code[0]
 #       data2 = code[1]
#       data3 = code[2]

#    return data1, data2, data3

def mess():
    time.sleep(0.2)
    serialline = ser.readline()
    s = ''
    for a in serialline:
        s += chr(a)
    f1.write(s)
    print(s)
    if s:
        return 1
    else:
        return 0
  #  data1,data2,data3 = ork()
  #  f1.write(data1)
  #  print(data1)
 #   f1.write(' ')
 #   print(' ')
  #  print(data2)
  #  f1.write(data2)
  #  f1.write(' ')
  #  print(' ')
  #  print(data3)
  #  f1.write(data3)
i = 0
print('start')
while 1:
    if ser.read(5):
        break

while i < 200:
    try:
        mess()
        q = mess()
        if q == 1:
            i = i + 1
    except KeyboardInterrupt:
        break
f1.write("STOP")
ser.write(2)
ser.close()
f1.close()