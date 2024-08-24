N, M = map(int, input().split())


def recursive(n, i, seq):
    if n == M:
        print(*seq)

    for j in range(i, N + 1):
        seq.append(j)
        recursive(n + 1, j + 1, seq)
        seq.pop()


recursive(0, 1, [])
