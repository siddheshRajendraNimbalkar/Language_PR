class Basic:
    def List1():
        List1 = ["apple","mango"]
        List1.append("orange")
        return List1
    
    def Object1():
        student = {
            "name": "John",
            "age": 36,
            "country": "Norway"
        }

        return student
    
    def ListComprehension():
        list2 = [x**2 for x in range(1,11)]
        return list2

print(Basic.List1())
print(Basic.Object1())
print(Basic.ListComprehension())