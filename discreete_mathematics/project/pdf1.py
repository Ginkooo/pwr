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


def mod(x, y):
    return x - y*floor(x/y)


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


def permutations_len_n(set, prefix, n, k):
    if (k == 0):
        if is_permutation(prefix):
            yield prefix
        return
    for i in range(n):
        new_prefix = prefix + (set[i],)
        yield from permutations_len_n(set, new_prefix, n, k - 1)


digits = list(range(10))
for perm in permutations_len_n(digits, (), len(digits), 5):
    print(perm)
