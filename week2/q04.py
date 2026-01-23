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

num = int(input("Enter a number: "))

if is_narcissistic_number(num):
    print(f"{num} is an narcissistic number.")
else:
    print(f"{num} is not an narcissistic number.")