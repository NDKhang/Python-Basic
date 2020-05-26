#  Code4Life TEAM - Python cơ bản

# Loops là gì?
# Tạo sao dùng loops trong lập trình

# Dạng 01: Vòng lặp FOR - FOR LOOPS ......................................................
# Loại 1: For theo phần tử
mylist = ["Code4Life", "Python", "C#", "SQL", "PHP", "Fortran", "C++"]
for x in mylist:
    print(x)

mylist = [1, 2, 3, 10, 11, 12, 20]
for x in mylist:
    print(x)

name = "Code4Life"
for i in name:
    print(i)

# loại 2: For theo thứ tự (Index)
for x in range(6):
    print(x)

for x in range(2, 30, 3):
    print(x)

#  Vòng lặp lồng nhau
mylist = ["Code4Life", "Python", "C#"]
thislist = ["SQL", "PHP", "Fortran", "C++"]

for x in mylist:
    for y in thislist:
        print(x, y)

# Câu điều kiện trong vòng lặp
mylist = ["Code4Life", "Python", "C#"]
for x in mylist:
    if x == "Python":
        print(x)
    else:
        print("Không phải là Python")


# Dạng 02: Vòng lặp WHILE ...................................................................
i = 1
while i < 6:
  print(i)
  i += 1


# Các lệnh tác động đến vòng lặp
i = 0
while i < 6:
  i += 1
  if i == 3:
    continue
  print(i)

i = 1
while i < 6:
  print(i)
  if i == 3:
    break
  i += 1