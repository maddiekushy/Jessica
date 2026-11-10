def collatz(n):
    x = 0
    if n == 1:
        return x
    if n % 2 == 0:
        x += collatz(int(n / 2)) + 1
    elif n % 2 != 0:
        x += collatz(int(3 * n + 1)) + 1
    return x

print(collatz(42))