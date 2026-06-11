# a  = [1,2,3,5,8,0]
a = [-1,4,-2,3,0]
a.sort()
print(a)
for i,v in enumerate(a):
    if i < len(a)-1:
        diff = a[i+1] - a[i]
        if diff > 1:
            for c in range(a[i]+1,a[i+1]):
                print(c)

    