# Smallest multiple
#
# 2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
# What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?

i = 2520
c = False
r = (3, 6, 7, 8, 9, 11, 12, 13, 14, 15, 16, 17, 18, 19)
while c is False:
    for j in r:
        if i % j == 0:
            c = True
            continue
        else:
            c = False
            break
    i += 20  # Только четные

print(i - 20)
