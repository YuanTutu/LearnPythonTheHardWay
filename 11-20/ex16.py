from sys import argv

script,filename = argv

print(f"we are going to erase {filename}")
print(f"if you dont want that ,hit ctrl-c(^c)")
print("if you do want that ,hit return.")

input("?")

print("openning the file...")
target = open(filename,'w')

print("truncating the file .goodbye~")
target.truncate()

print("now i am going to ask you for three lines")

line1 = input("line1:")
line2 = input("line2:")
line3 = input("line3:")

print("i am going to write these to the file.")
target.write(line1)
target.write("\n")
target.write(line2)
target.write("\n")
target.write(line3)
target.write("\n")

print("and finally,we close it.")
target.close()
