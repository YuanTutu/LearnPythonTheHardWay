class Parent(object):

    def implicit(self):
        print("PARENT implicit()")

class Child(Parent):
    pass

dad = Parent()
son = Child()

dad.implicit()
print(">>> dad=",dad)
print(">>> Parent",Parent)
son.implicit()
print(">>> son=",son)
print(">>> Child=",Child)
