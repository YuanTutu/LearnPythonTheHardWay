class Parent(object):

    def override(self):
        print("PARENT override()")

class Child(Parent):

    def override(self):
        #print(">>> override",override)---------# BUG: 
        print("CHILD override()")

dad = Parent()
son = Child()

dad.override()
print(">>> dad=",dad)
print(">>> Parent",Parent)
son.override()
print(">>> son=",son)
print(">>> Child=",Child)
