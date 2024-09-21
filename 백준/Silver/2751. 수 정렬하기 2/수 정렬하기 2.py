import sys
t=int(sys.stdin.readline())
s=[]
for i in range(t):
    s.append(int(sys.stdin.readline()))
s.sort()
for i in s:
    print(i)