n = int(input())

a = (n % 1440) // 60
b = (n % 1440) % 60

print(a)
print(b)