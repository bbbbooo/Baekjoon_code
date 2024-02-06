import sys

while True:
    a, b, c = map(int, sys.stdin.readline().rstrip().split())

    if a == 0 and b == 0 and c == 0:
        break

    a2 = a**2
    b2 = b**2
    c2 = c**2

    if a2 + b2 == c2 or a2 + c2 == b2 or b2 + c2 == a2:
        print('right')
    else:
        print('wrong')
