s1 = "listen"
s2 = "silent"

s1 = list(s1)
s2 = list(s2)

# sort

def SortFunc(s1):
    for i,v in enumerate(s1):
        for j in range(i+1,len(s1)):
            if s1[i] > s1[j]:
                s1[i],s1[j] = s1[j],s1[i]
    return s1

print(SortFunc(s1))
print(SortFunc(s2))
print(SortFunc(s1) == SortFunc(s2))
