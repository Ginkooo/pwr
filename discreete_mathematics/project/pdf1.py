def cealing(x):
    if x < 0:
        return int(x)
    has_rest = x - int(x) != 0
    return int(x)+1 if has_rest else x


def floor(x):
    if x > 0:
        return int(x)
    has_rest = x - int(x) != 0
    return int(x)-1 if has_rest else x


def fractional_part(x):
    return x - floor(x)


def first_primes(n):
    primes = []
    possible_prime = 2
    while True:
        for i in range(2, possible_prime):
            if possible_prime % i == 0:
                break
        else:
            primes.append(possible_prime)
        possible_prime += 1
        if len(primes) == n:
            return primes


def is_permutation(seq):
    unique = set()
    for e in seq:
        if e in unique:
            return False
        unique.add(e)
    return True
