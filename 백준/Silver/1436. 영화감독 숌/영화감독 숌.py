import sys

n = int(sys.stdin.readline().strip())
s = 666

while n:
    if '666' in str(s):
        n-=1
    s += 1

print(s-1)
