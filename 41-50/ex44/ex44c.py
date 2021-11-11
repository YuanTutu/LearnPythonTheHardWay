class Parent(object):

    def altered(self):#altered改变
        print("PARENT altered()")

class Child(Parent):

    def altered(self):
        print("CHILD,BEFORE PARENT altered()")
        super(Child,self).altered()
        print("CHILD,AFTER PARENT altered()")

dad = Parent()
son = Child()

dad.altered()
print(">>> dad=",dad)
print(">>> Parent",Parent)
son.altered()
print(">>> son=",son)
print(">>> Child=",Child)
