#  Code4life TEAM .................................................

# 01_ Caau lenh If
a = 33
b = 200
if b > a:
    print("b lon hon a")

if b < a:
    print("b nho hon a")

# 02_Cau lenh If-else (cau truc re nhanh 2 truong hop)
a = 33
b = 200

if b < a:
    print("b nho hon a")
else:
    print("b lon hon hoac = a")

#  03_ Cau lenh If-elif-else (cau truc re nhanh nhieu hon 2 truong hop)
a = 33
b = 200

if b < a:
    print("b nho hon a")
elif a == b:
    print("b bang a")
else:
    print("b lon hon a")


#  Mot so vi du............................

#  vi du 1:
tb = 8.5
if (tb >= 0 and tb < 3.5):
    print('Hoc sinh kem')
elif (tb >= 3.5 and tb < 5):
    print('Hoc sinh yeu')
elif (tb >= 5 and tb < 6.5):
    print('Hoc sinh trung binh'):
elif (tb >= 6.5 and tb < 8):
    print('Hoc sinh kha')
else:
    print('Hoc sinh goi')

#  vi du 2:
tb = 8.5
if (a >= 0 and a <= 10):
    if (tb >= 0 and tb < 3.5):
        print('Hoc sinh kem')
    elif (tb >= 3.5 and tb < 5):
        print('Hoc sinh yeu')
    elif (tb >= 5 and tb < 6.5):
        print('Hoc sinh trung binh'):
    elif (tb >= 6.5 and tb < 8):
        print('Hoc sinh kha')
    else:
        print('Hoc sinh goi')
else:
    print('Diem khong hop le')