import sys
from collections import deque

input = sys.stdin.readline

N = int(input())
arr = []

for _ in range(N):
    arr.append(int(input()))
arr.sort()

print("\n".join(str(c) for c in arr))
