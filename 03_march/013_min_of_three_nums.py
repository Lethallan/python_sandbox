a = int(input())
b = int(input())
c = int(input())

if b > a < c or b == c > a or a == b < c:
    print(a)
elif a > b < c or a == c > b or a == c < b:
    print(b)
elif b > c < a or a == b > c or b == c < a:
    print(c)
else:
    print('what?!')