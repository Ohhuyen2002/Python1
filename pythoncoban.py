#Tao 1 tuple
x=1
print(x)
day=('ngay 1', 'ngay 2', 'ngay 3')
print(day)
tiengAnh={'dictionary': 'tu dien', 'crazy':'dien','name':'ten'}
tiengHan={'오찬솔': 'OhChansol', '검퓨터': 'may tinh', '울다':'khoc'}
print(tiengHan)
print(tiengHan['검퓨터'])
tiengHan['울다']='khok'
print(tiengHan)
del tiengHan['오찬솔']
print(tiengHan)
ngoaingu={'ten':'Huyen', 'ngonngu': {'English':'tieng Anh', 'Korean':'Tieng Han'}}
print(ngoaingu)
print(ngoaingu['ngonngu']['English'])
a=2
b=5
print(a==b)
print(a!=b)
print(a<b)
print(a>b)
print(a<=b)
print(a>=b)
x=[1, 2, 3, 4, 5, 6]
print(a in x)
print(a not in x) #False
a=2
b=3
if(a==b):
    print('dung roi!')
    print('hí hí')
else:
    print('u')
print (a is b)
print(a is not b)
a=10
if(a>0):
    print('duong')
elif(a<0):
    print('am')
else:
    print('u duong u am')
ten="Oh Huyen"
for i in ten:
    print(i)
for i in range(0, 10): #range (a,b); từ a đến b-1, cách 1 đơn vị
    print(i)
i=22
while i>10:
    print(i)
    i-=2
def tinhTong(a, b):
    return (a+b)
print(tinhTong(2,3))
def tinhhieu(a, b=2):
    return (a-b)
a=10
print(tinhhieu(a))
o=2
def value():
    global o
    o=4
    print(o)
value()
print(o)
def tinhtong(*n):
    sum=0
    for i in n:
        sum+=i
    return (sum)
print(tinhtong(2, 3,4 , 1))
file=open('oh.txt')
data=file.read()
file.close()
print(data)
