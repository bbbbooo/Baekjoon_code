import sys

n = int(sys.stdin.readline().rstrip())
count = [0] * 10001
for i in range(n):
    no = int(sys.stdin.readline().rstrip())
    count[no] += 1

for i in range(len(count)):
    for j in range(count[i]):
        print(i)