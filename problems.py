#!/opt/homebrew/bin/python3

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

def main():
    print(problem2())


if __name__ == "__main__":
    main()
