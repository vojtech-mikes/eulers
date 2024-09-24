import math

def is_prime(x):
        if x < 2:
            return False

        y = round(math.sqrt(x))
        for i in range(2, y+1):
            if x % i == 0:
                return False

        return True
