# Largest palindrome product
#
# A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers
# is 9009 = 91 × 99. Find the largest palindrome made from the product of two 3-digit numbers.


list_1 = []
for i in range(999, 100, -1):
    for j in range(999, 100, -1):
        c = i * j
        if str(c) == str(c)[::-1]:
            list_1.append((c, i, j))
print(list_1)
print(max(list_1))


def solution():
    res = max(i * j for i in range(999,100,-1) for j in range(999, 100, -1) if str(i * j) == str(i * j)[::-1])
    return res

print(solution())