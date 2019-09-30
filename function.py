import math
funcs={"sqrt":math.sqrt,"log":math.log,"log10":math.log10}
f="start"
while f != "stop":
    n=int(input("enter number: "))
    f=input("function to perform (or stop): ")
    if not f in funcs:
            print("No such function")
    else:
            print("Applying function %s to %f yields %f"%(f,n,funcs[f](n)))
            
