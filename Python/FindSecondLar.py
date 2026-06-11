a = list("1234567890")
b = [int(v) for v in a]

def find_second_largest(arr):
    arr.sort()
    return arr[-2]

print(find_second_largest(b))