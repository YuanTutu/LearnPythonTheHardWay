print("let's practice everything.")
print('you\'d need to know \'bout escapes with \\ that do:')
print('\n newlines and \t tabs.')

poem = """
\tThe lovely world
with
cannot discern \n the needs of love
nor
and
\n\t\twhere there is none.
"""

print("----------")
print(poem)
print("----------")


five = 10 - 2 + 3 -6
print(f"this should be five:{five}")

def secret_formula(started):
    jelly_beans = started * 500
    jars = jelly_beans / 1000
    crates = jars / 100
    return jelly_beans,jars,crates#jelly_beans会被在30行转换成beans


start_point = 10000
beans,jars,crates = secret_formula(start_point)#jelly_beans会被在30行转换成beans，或者说返回值对应到了beans

#remember that this is another way to format a string
print("with a starting point of:{}".format(start_point))
#it is just like with an f"" string
print(f"we'd have {beans} beans,{jars} jars,and {crates} crates.")

start_point = start_point / 10

print("we can also do that this way:")
formula = secret_formula(start_point)
#this is an easy way to apply a list to a format string
print("we'd have {} beans,{} jars,and {} crates.".format(*formula))
