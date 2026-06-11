def decorator(func):
    def wrapper():
        print("Before")
        func()
        print("After")
    return wrapper

def add(a,b):
    print(a+b)

decorator(add(1,2))