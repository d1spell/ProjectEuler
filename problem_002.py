# Even Fibonacci numbers
#
# Each new term in the Fibonacci sequence is generated by adding the previous two terms. By starting with 1 and 2,
# the first 10 terms will be: 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ... By considering the terms in the Fibonacci
# sequence whose values do not exceed four million, find the sum of the even-valued terms.

from assistant import execution_time


@execution_time
def solution(n=4000000):
    a = 0
    b = 1
    res = 0
    while a < n:
        if a % 2 == 0:
            res += a
        a, b = b, a + b

    return res


if __name__ == '__main__':
    print(solution())
