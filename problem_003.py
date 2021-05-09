# Largest prime factor
#
# The prime factors of 13195 are 5, 7, 13 and 29.
# What is the largest prime factor of the number 600851475143 ?


def solution(n=600851475143):
    d = 2
    while d * d <= n:
        if n % d == 0:
            n //= d
        elif d == 2:
            d += 1
        else:
            d += 2
    if n > 1:
        return n


print(solution())
