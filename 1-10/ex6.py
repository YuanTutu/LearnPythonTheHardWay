type_of_people = 10
x = f"There are {type_of_people} types of people."

binary = "binary"
do_not = "don't"
y = f"those who know {binary} and those who {do_not}"

print(x)
print(y)

print(f"i said:{x}")
print(f"i also also:'{y}'")

hilarious = "False"
joke_evaluation = "isn't that joke so funny?!{}"

print(joke_evaluation.format(hilarious))

w = "this is the left side of ..."
e = "a string with a right side."

print(w+e)
