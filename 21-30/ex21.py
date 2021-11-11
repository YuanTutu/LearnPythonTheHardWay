def add(a,b):
    print(f"ADDING {a} + {b}")
    return a + b

def subtract(a,b):
    print(f"SUBSTRACTING {a} - {b}")
    return a - b

def multiply(a,b):
    print(f"MULTIPLYING {a} * {b}")
    return a * b

def divide(a,b):
    print(f"DIVIDING {a} / {b}")
    return a / b


print("lets do some math with just functions!")

age = add(30,5)
print(">>> age=",age)
height = subtract(78,4)
print(">>> height=",height)
weight = multiply(90,2)
print(">>> weight=",weight)
iq = divide(100,2)

print(f"age:{age},height:{height},weight:{weight},iq:{iq}")


#a puzzle for the extra credit,type it in anyway
print("here is a puzzle.")
#puzzle 迷，迷惑  extra credit额外分
what = add(age,subtract(height,multiply(weight,divide(iq,2))))

print("that becomes: ",what,"can you do it by hard?")
