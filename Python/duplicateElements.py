num = [1,2,1,3,4,4,5,3,2,8,6,6]

duplicate = []

for n in num:
    if num.count(n) > 1 and n not in duplicate:
        duplicate.append(n)

print(duplicate)