#  Code4life TEAM .................................................
print("Hello")
print('Hello')

# gan bien bang chuoi
a = "Hello"
print(a)

# Chuoi nhieu dong - Multiline Strings
a = """Team Code4life xin chao cac ban,
day la khoa hoc Python co ban,
Code4life con co rat nhieu khoa hoc lap trinh va cuoc song thu vi khac
# Mong cac ban theo doi! """
print(a)

# Chuoi la mot mang ky tu
a = "Hello, World!"
print(a[1])
print(a[2:5])
print(a[7:12])
print(a[-5:-2])

#  Do dai chuoi
a = "Hello, World!"
print(len(a))

# Thao tac tren chuoi
a = " Hello, World! "
print(a.strip())
print(a.lower())
print(a.upper())
print(a.replace("World", "Code4life"))
print(a.split(","))

#  Ghep chuoi - String Concatenation
a = "Hello"
b = "World"
c = a + b
print(c)
c = a + " " + b
print(c)

# Format chuoi
you = "Ban"
loichao = "Chao mung %s den voi Code4life" % (you)
print(loichao)

you = "Ban"
ad = "Code4life"
loichao = "Chao mung %s den voi %s" % (you, ad)
print(loichao)

you = "Ban"
soVideo = 5
loichao = "Chao mung {0} den voi Video so {1} khoa hoc Python co ban"
print(myorder.format(you, soVideo))

you = "Ban"
soVideo = 5
ad = "Code4life"
loichao = "Chao mung {1} den voi Video so {2} khoa hoc Python co ban cua {0}"
print(myorder.format(ad, you, soVideo))
