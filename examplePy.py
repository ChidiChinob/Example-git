import sys

randomlist = ['a', 0, 2]

for entry in randomlist:
    try:
        print("the entry is",entry)
        r = 1/int(entry)
        break
    except:
        print("oops!",sys.exc_info()[0],"occured")
        print("next entry")
        print()
print("The reciprocal of ",entry, " is", r)

