li = [6, 7, 2, 4]
n = 72
combos = []
L, R = 0, 0

while L <= len(li) - 1:
    while R <= len(li) - 1:
        x = int("".join(map(str, li[L:R])))
        if x <= n:
            combos.append(x)
        R += 1
    L+=1
        

print(combos)

# l = [1, 2, 3]
# x = int("".join(map(str, l)))
# print(x)
