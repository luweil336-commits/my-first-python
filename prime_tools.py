# 素数工具：判断素数 + 输出前 100 个素数

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

count = 0
x = 2
while count < 100:
    if is_prime(x):
        print(x)
        count += 1
    x += 1