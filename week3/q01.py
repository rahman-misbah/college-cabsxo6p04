from math import log2

# Check if power of 2
def power_of_2(num: int) -> bool:
    return num > 0 and num & (num - 1) == 0

num = int(input("Enter a number to check if its a power of 2: "))

if(power_of_2(num)):
    print(f"{num} is power of 2 (for k = {int(log2(num))})")
else:
    print(f"{num} is not a power of 2")