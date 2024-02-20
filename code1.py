def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

prime_numbers = [n for n in range(1001) if is_prime(n)]
total = sum(prime_numbers)

print("Prime numbers from 0 to 1000:", prime_numbers)
print("Total sum of prime numbers:", total)