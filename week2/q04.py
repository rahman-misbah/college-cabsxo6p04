# Armstrong Numbers
def is_narcissistic_number(num):
    num_backup = num
    num_len = len(str(num))
    sum_of_powers = 0

    while num > 0:
        digit = num % 10
        sum_of_powers += digit ** num_len
        num //= 10
    
    return sum_of_powers == num_backup

n = int(input("Enter value of n: "))

for i in range((10**(n-1)), (10**n)):
    if is_narcissistic_number(i): print(i)