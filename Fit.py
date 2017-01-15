from sklearn.externals import joblib
from sklearn.svm import SVC
import os

x = []
l = []
y = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
basedir = os.path.abspath(os.path.dirname(__file__))
f = open('data1.log', 'r')
svm = SVC()
def read():
    fline = f.readline().split('\n')
    code = []
   # data1 = "0"
   # data2 = "0"
   # data3 = "0"
    code = fline[0].split(',')
    print(int(code[0]))
    print(code[1])
    print(code[2])
    l.append(int(code[0]))
    l.append(int(code[1]))
    l.append(int(code[2]))
    #if fline:
     #   code = fline[0].split(',')
      #  data1 = code[0]
       # data2 = code[1]
        #data3 = code[2]
 #   l.append(int(data1))
 #   l.append(int(data2))
 #   l.append(int(data3))


i = 0
while i < 20:
    i = i + 1
    fline = f.readline().split('\n')
    print(fline[0])
    j = 0
    while j < 200:
        read()
        j = j + 1
    x.append(l)
svm.fit(x, y)
joblib.dump(svm, os.path.join(basedir, 'rf.pkl'))
print("Learned")
f.close()
