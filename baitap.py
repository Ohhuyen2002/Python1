#Bài 1 tự làm
a="oh "
b= "huyen"
c= a+b
print(c)
chuoi=""
for i in range(2000, 3201):
    if(i%7==0 and i%5!=0):
        chuoi=chuoi+ str(i)+ ","
print(chuoi)
#bài 1 tham khảo trên mạng
j = []
for i in range (2000,3201):
    if (i % 7 == 0) and (i % 5 != 0):
        j.append(str(i)) #tenlist.append(data) : them data vào cuối list
print(",".join(j)) # 'dâu phân cách'.join(tenlist): biển list/tuple thành chuỗi và các phần tử cách nhau bởi dấu phân cách
#Bài 2
so=int(input("Nhập số vào: "))
giaithua=1
for i in range(1,so+1):
    giaithua*=i
print(str(giaithua))
#Bài 3
n=int(input("Nhập n= "))
dic={}
for i in range(1,n+1):
    dic[i]=i*i
print(dic)
#Bài 4
a=input('Nhập chuỗi số vào: ')
lst=a.split(',')
tup=tuple(lst)
print(lst)
print(tup)
#Bài 5
# có class bên python nâng cao nên chừa ra:>, nào học thì làm
#Bài 6
def tinh_BP(a):
    print(a**2)
tinh_BP(3)
#Bài 7, bài này xem code trên mạng nè
# ___doc___ là tài liệu có sẵn trong python, mình sẽ dùng
#abs, int, input để xuất định nghĩ có trong tài liệu này ra
print (abs.__doc__)
print (int.__doc__)
print (input.__doc__)
def square(num):
    return num ** 2
print (square.__doc__)

#Bài 8, class bỏ qua :>
#Bài 9
#Bài 25
n=int(input('Nhap so luong so: '))
for i in range(0, 3):
    lst[i]=int(input('Nhap so '))


    
                

        