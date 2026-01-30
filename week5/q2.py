def brute_force(passwd: int, passwd_len: int) -> int:
    count = 0

    for attempt in range(0, 10**passwd_len):
        count += 1

        if attempt == passwd:
            break
    
    return count

passwd = int(input("Enter a number: "))
passwd_len = len(str(passwd))

print(f"Password {passwd} of length {passwd_len} cracked in {brute_force(passwd, passwd_len)} attempts")