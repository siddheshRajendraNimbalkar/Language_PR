a = "machinelearning"

print(a[::-1])

# Without Slicing

rev = ""

for i in a:
    rev = i + rev

print("Without Slicing")
print(rev)