from sys import argv
from os.path import exists

script,from_file,to_file = argv

print(f"copying from {from_file} to {to_file}")

#we could do these two on one line,how?
in_file = open(from_file)
print(">>>> in_file=",repr(in_file))
indata = in_file.read()

print(f"the input file is {len(indata)} bytes long.")

print(f"does the output file exist?{exists(to_file)}")
print("ready,hit enter to continue,ctrl-c to abort.")
input()

out_file = open(to_file,'w')
out_file.write(indata)

print("alright,all done.")

out_file.close()
in_file.close()
