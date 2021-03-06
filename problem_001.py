# Multiples of 3 and 5
#
# If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9.
# The sum of these multiples is 23.
# Find the sum of all the multiples of 3 or 5 below 1000.
from assistant import execution_time


@execution_time
def solution():
    return sum(x for x in range(1, 1000) if x % 3 == 0 or x % 5 == 0)


if __name__ == '__main__':
    print(solution())
