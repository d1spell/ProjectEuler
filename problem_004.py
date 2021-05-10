# Largest palindrome product
#
# A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers
# is 9009 = 91 × 99. Find the largest palindrome made from the product of two 3-digit numbers.
from assistant import execution_time


@execution_time
def solution():
    res = max(i * j for i in range(999, 100, -1) for j in range(999, 100, -1) if str(i * j) == str(i * j)[::-1])
    return res


if __name__ == '__main__':
    print(solution())
    print(sketch())
