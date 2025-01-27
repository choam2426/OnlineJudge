from bisect import bisect_left, bisect_right

N = int(input())
cards = list(map(int, input().split()))
cards.sort()
M = int(input())
for target in map(int, input().split()):
    print(1 if bisect_left(cards, target) != bisect_right(cards, target) else 0, end=" ")
