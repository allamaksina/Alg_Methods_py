
# linear complexity
def gcd_naive(a, b):
    for d in range(min(a, b), -1, -1):
        if not d or a % d == b % d == 0:
            return d


print(gcd_naive(45, 30))
print(gcd_naive(0, 0))


def gcd_euclid(a, b):
    assert a >= 0 and b >= 0
    while a and b:
        if a >= b:
            a %= b
        else:
            b %= a
    return max(a, b)


print(gcd_euclid(1000, 800))


def gcd_euclid2(a, b):
    assert a >= 0 and b >= 0
    if not a or not b:
        return max(a, b)
    else:
        return gcd_euclid2(b % a, a)


print(gcd_euclid2(2049587609568883254798, 9763947638))

