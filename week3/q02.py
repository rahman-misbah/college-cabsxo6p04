# Mersenne Primes
def power_of_2(num: int) -> bool:
    return num > 0 and num & (num - 1) == 0

def is_prime(n: int) -> bool:
    if n < 2: return False
    
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def is_mersenne_prime(num: int) -> bool:
    return is_prime(num) and power_of_2(num + 1)

num = int(input("Enter a number: "))

if is_mersenne_prime(num):
    print(f"{num} is a mersenne prime")
else:
    print(f"{num} is not a mersenne prime")