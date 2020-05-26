#  Code4life TEAM .................................................

#  Khai bao bien
a = 10
print("so a=", a)
b = 3
print("so b=", b)

# 01_ Toan tu so hoc - Arithmetic Operators (+  -  *  /  %  **  //)
a + b
print(a + b)
print("phep tru", a - b)
print("phep nhan", a * b)
print("phep chia", a / b)
print("phep chia lay so du", a % b)
print("luy thua", a ** b)
print("chia lam tron xuoong", a // b)

# 02_ Toan tu so sanh - Comparison Operators (==  !=  <  >  <=  >=)
print("==", a == b)
print("!=", a != b)
print("<", a < b)
print(">", a > b)
print("<=", a <= b)
print(">=", a >= b)

# 03_ Toan tu gan - Assignment Operators (=  +=  -=  *=  /=  %=   **=  //=)
a = 10
c = a
print("c = a", c)

c = 3
c += a
print("c += a (tương đương với c = c + a)", c)

c -= a
print("c -= a (tương đương với c = c - a)", c)

c *= a
print("c *= a (tương đương với c = c * a)", c)

c *= a
print("c /= a (tương đương với c = c / a)", c)

c %= a
print("c %= a (tương đương với c = c % a)", c)

c **= a
print("c **= a (tương đương với c = c ** a)", c)

c //= a
print("c //= a (tương đương với c = c // a)", c)

# 04_ Toan tu logic - Logical Operators (and  or  not)
x = 5
print(x < 5 and x < 10)
print(x > 3 or x < 4)
print(not(x > 3 and x < 10))

# 05_Toan tu xac thuc - Identity Operators (is  is not)
x = ["Code4Life", "Python", "list"]
y = ["Code4Life", "Python", "list"]
z = x
print(x is z)
print(x is y)
print(x == y)
print(x is not y)

# 06_Toan tu thanh vien - Membership Operators (in  not in)
x = "code4life"
print("code" in x)
print("4" in x)
print("5" in x)
print(4 in x)
print("5" in not x)
