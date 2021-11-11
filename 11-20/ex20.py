from sys import argv

script,input_file = argv

def print_all(f):
    #print(">>> print_all:f=",f)
    print(f.read())
    #print("<<< print_all:f=",f)

def rewind(f):
    f.seek(0)

def print_a_line(line_count,f):
    print(line_count,f.readline())
#begin
current_file = open(input_file)

print("first lets print the whole file:\n")

print_all(current_file)

print("Now lets rewind,kind of like a tape.")

rewind(current_file)

print("lets print three lines:")

current_line = 1
print_a_line(current_line,current_file)

current_line = current_line + 1
print_a_line(current_line,current_file)

current_line = current_line + 1
print_a_line(current_line,current_file)
