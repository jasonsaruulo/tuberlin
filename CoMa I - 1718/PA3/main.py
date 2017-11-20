"""
Calculates the representative of "a modulo m" from {k, k + 1, ..., k + m - 1}.

Let k be an integer and m a natural number except 0. For every integer a there
is an integer p and number q within {k, k + 1, ..., k + m - 1} with

a = p * m + q.

The number q is called the "representative of a modulo m from
{k, k + 1, ..., k + m - 1}".
"""
def repraesentant(a, m, k):
    q = k
    p = (a - q) / m
    while not float(p).is_integer() and q <= k + m - 1:
        q += 1
        p = (a - q) / m
    return q


"""
Calculates for a given integer z the representative of "z modulo 2^l" from
{0, ..., 2^l - 1}.
"""
def f(z, l):
    k = 0
    m = 2 ** l
    return repraesentant(z, m, k)


"""
Calculates for a number r from {0, ..., 2^l - 1} its representative modulo 2^l
from {-2^(l - 1), -2^(l - 1) + 1, ..., 2^(l - 1) - 2, 2^(l - 1) - 1}
"""
def umkehrfunktion_von_f(r, l):
    k = -2 ** (l - 1)
    m = -2 * k
    return repraesentant(r, m, k)


# print("repraesentant(10, 5, 11): " + str(repraesentant(10, 5, 11)))
# print("f(3, 4): " + str(f(3, 4)))
# print("f(-3, 4): " + str(f(-3, 4)))
# print("umkehrfunktion_von_f(3, 5): " + str(umkehrfunktion_von_f(3, 5)))
# print("umkehrfunktion_von_f(16, 5): " + str(umkehrfunktion_von_f(16, 5)))
# print("f(2, 4) + f(-2, 4): " + str(f(2, 4) + f(-2, 4)))
