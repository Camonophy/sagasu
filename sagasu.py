#!/usr/bin/python3
 
import sys
import subprocess

from binaryornot.check import is_binary

print()
args = sys.argv[1:len(sys.argv)]    # Search terms

# Current dir
output = str(subprocess.check_output(["ls"]))
output = output[2:len(output)-3].split("\\n")

while output != []:
    file = output.pop(0)
    ls = str(subprocess.check_output(["ls", file]))
    if(ls[2:len(ls)-3] == file and not(is_binary(file, False))):                # Check, whether it is a file
        for arg in args:
            try:
                found = str(subprocess.check_output(["grep", "-n", arg, file]))
                print("#### " + file + " ####")
                lines = found[2:len(found)-3].split("\\n")
                for line in lines:
                    print("\t"+line)
                print()
            except:
                continue
    elif(is_binary(file, False)):
        continue
    else:                                       # Extract dir
        for el in ls[2:len(ls)-3].split("\\n"):
            output.append(file+"/"+el)

print()
