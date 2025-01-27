N = int(input())
cards = list(map(int, input().split()))
card_map = {card: 1 for card in cards}
M = int(input())
for target in map(int, input().split()):
    print(card_map.get(target, 0), end=" ")