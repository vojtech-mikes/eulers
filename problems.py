#!/opt/homebrew/bin/python3
import math
import utils

def problem1():
    solution = sum(x for x in range(1000) if x % 3 == 0 or x % 5 == 0)
    return solution


def problem2():
    x = 1
    y = 2
    z = 0
    total = 2

    while z < 4_000_000:
        z = x + y
        if z % 2 == 0:
            total += z
        x = y
        y = z

    return total


def problem3():
    x = 600851475143
    p = 0
    sr = round(math.sqrt(x))

    for i in range(2, sr+1):
        if x % i == 0:
            x = x/i
            if utils.is_prime(i):
                p = i

    return p

def problem7():
    c = 0
    p = 0
    n = 0
    while c < 1_0001:
        if utils.is_prime(n):
            p = n
            c += 1

        n += 1

    return p

def main():
    print(problem7())


if __name__ == "__main__":
    main()
