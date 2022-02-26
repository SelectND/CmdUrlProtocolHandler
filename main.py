import os
import sys

nativearg = (sys.argv[1])
usablearg = nativearg.replace("cmd://", "")

print("This reached the parser: " + nativearg)


while True:
    ifrun = input("Do you really want to run it? [y/n] ")
    if (ifrun == "y"):
        os.system("cmd /c " + usablearg)
        break

    elif(ifrun == "n"):
        print("aborting... ")
        break
    else:
        print("Couldn't understand you. Please do it again.")
        continue


 
