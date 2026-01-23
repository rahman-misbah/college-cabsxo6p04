# Relatively Prime (Coprime)

def gcd(x, y):
    if x < 0 or y < 0:
        return -1
    
    while(y):
        x, y = y, x % y
    return x

def is_coprime(a: int, b: int) -> bool:
    factor = gcd(a, b)
    return factor == 1

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

if(is_coprime(a, b)):
    print(f"{a} and {b} are relatively primes")
else:
    print(f"{a} and {b} are not relatively primes")