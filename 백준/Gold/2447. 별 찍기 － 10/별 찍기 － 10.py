def draw_star(n):
    if n == 1:
        return ["*"]
    
    stars = draw_star(n // 3)
    L = []
    
    for s in stars:
        L.append(s * 3)
    for s in stars:
        L.append(s + " " * (n // 3) + s)
    for s in stars:
        L.append(s * 3)
    
    return L

N = int(input())
print("\n".join(draw_star(N)))