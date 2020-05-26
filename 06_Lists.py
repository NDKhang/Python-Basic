#  Code4Life TEAM - Python cơ bản

# List là gì?
#  List là một dạng dữ liệu cho phép lưu trữ nhiều kiểu dữ liệu khác nhau trong nó
mylist = ["Code4Life", "Python", "list"]
print(mylist)

# Có thể truy xuất đến các phần tử bên trong nó thông qua vị trí của phần tử đó trong list
mylist = ["Code4Life", "Python", "list"]
print(mylist[1])
print(mylist[-1])
print(mylist[1:2])

thislist = ["Code4Life", "Python", "C#", "SQL", "PHP", "Fortran", "C++"]
print(thislist[:4])
print(thislist[2:])

# Thay đổi thành phần trong list
thislist = ["Code4Life", "Python", "list"]
thislist[1] = "SQL"
print(thislist)

#  Kiểm tra thành phần có trong list
thislist = ["Code4Life", "Python", "list"]
if "Python" in thislist:
  print("Yes, 'Python' is in the fruits list")

# Số lượng thành phần trong list
thislist = ["Code4Life", "Python", "list"]
print(len(thislist))

# Thêm thành phần cho list
thislist = ["Code4Life", "Python", "list"]
thislist.append("SQL")
print(thislist)

thislist = ["Code4Life", "Python", "list"]
thislist.insert(1, "SQL")
print(thislist)

thislist.remove("SQL")
print(thislist)

#  Nối các list
list1 = ["a", "b" , "c"]
list2 = [1, 2, 3]
list3 = list1 + list2
print(list3)

list1 = ["a", "b" , "c"]
list2 = [1, 2, 3]
for x in list2:
  list1.append(x)
print(list1)

list1 = ["a", "b" , "c"]
list2 = [1, 2, 3]
list1.extend(list2)
print(list1)