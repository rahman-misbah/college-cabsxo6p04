# Order (k) of r^k = 1 (mod n)
def gcd(x, y):
    if x < 0 or y < 0:
        return -1
    
    while(y):
        x, y = y, x % y
    return x

def compute_order(r: int, n: int) -> int:
    if gcd(r, n) != 1: return 0

    k = 1

    while r**k % n != 1:
        k += 1
    
    return int(k)

r = int(input("Enter value of r: "))
n = int(input("Enter value of n: "))
k = compute_order(r, n)

if not k:
    print(f"Not Defined")
else:
    print(f"Order of {r} modulo({n}) is {k}")
