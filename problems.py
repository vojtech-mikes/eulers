#!/opt/homebrew/bin/python3

def problem1():
    solution = sum(x for x in range(1000) if x % 3 == 0 or x % 5 == 0)
    return solution


def main():
    print(problem1())


if __name__ == "__main__":
    main()
