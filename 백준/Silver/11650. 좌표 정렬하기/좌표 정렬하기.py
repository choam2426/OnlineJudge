import sys
input=sys.stdin.readline
N=(int(input()))
S1=[]
for i in range(N):
    S1.append(list(map(int,input().split())))

S1.sort()
for i in range(N):
    print(S1[i][0],S1[i][1])