# Euler Totient

def gcd(x, y):
    if x < 0 or y < 0:
        return -1
    
    while(y):
        x, y = y, x % y
    return x

def is_coprime(a: int, b: int) -> bool:
    factor = gcd(a, b)
    return factor == 1

def euler_totients(num: int) -> int:
    if num == 1: return 1

    count = 0

    for i in range(1, num):
        if is_coprime(i, num): count += 1
    
    return count

num = int(input("Enter a number: "))

print(f"Euler's Totients of {num} is {euler_totients(num)}")