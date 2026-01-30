a = [1, 2, 3, 2, 1]
b = [3, 2, 2, 3, 3, 2]

union = []
for i in a:
    if i not in union:
        union.append(i)
for i in b:
    if i not in union:
        union.append(i)
print(union)
