'''#1-topshiriq
for n in range (1,70):
    if n%8==0:
        print (n)
#2-topshiriq
yigindi=0
for n in range(10,31):
    yigindi=yigindi+n
    print(yigindi)
#3-topshiriq
yigindi=0
for n in range(2,101,2):
    yigindi=yigindi+n
print(yigindi)
#4-topshiriq
kopaytma=1
for n in range(1,11):
    kopaytma*=n
    print(kopaytma)
#5-topshiriq
kublar=[]
sonlar=list(range(1,11))
for son in sonlar:
        print(f"{son} ning kubi {son**3} ga teng")
#6-topshiriq
for n in range(1,101):
    if n%5==2:
       print(n)
darajalar=[]
for son in range(1,11):
    daraja=son*son*son*son
    darajalar.append(daraja)
print(darajalar)'''
son_1=int(input("1-sonni kiriting"))
son_2=int(input("2-sonni kiriting"))
if son_1<son_2:
    print("bu sonlardan kichigi",son_1)
else:
    print("bu sonlardan kichigi",son_2)
#uyga vazifa 3ta sonni kattasini topish
