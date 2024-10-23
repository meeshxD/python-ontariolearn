import pytest
def generate_prime_factors(n):
    if (not isinstance(n,int)):
        raise ValueError("Wrong data type, must be an integer")

    prime_factors = []
    if n == 1:
        return prime_factors
    prime_factors.append(n)
    if n == 2:
        return prime_factors
    if n>2:
        sign = 1
        x = 2
        while sign == 1:
            if x == prime_factors[-1]:
                sign = 0
            elif n % x == 0:
                if prime_factors[-1] % x == 0:
                    prime_factors.insert(-1,x)
                    y = prime_factors[-1]/x
                    prime_factors.insert(-1, int(y))
                    prime_factors.pop()
                    x = 2
                else:
                    x += 1
                    sign = 1
            else:
                x += 1
    return prime_factors