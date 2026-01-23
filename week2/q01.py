# Verify prime

def is_prime(n):
    if n < 1:
        return False, -1
    if n == 1:
        return False, 1
    
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False, i
    return True, n

x = int(input("Enter a positive integer: "))

prime, val = is_prime(x)

if prime:
    print(f"{x} is a prime number.")
else:
    if val == -1:
        print(f"{x} is not a valid input.")
    elif val == 1:
        print(f"{val} is not a prime number.")
    else:
        print(f"{val} is a factor of {x}.")