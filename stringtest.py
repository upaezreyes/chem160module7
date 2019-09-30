# break up a string into a list of characters using list()
string = "abcdefghi"
alist = list(string)
print(string)
print(alist)


# assemble a list of characters into a string using joing()
alist.reverse()   # reverse order of alist
newstring = " ".join(alist)
print(newstring)

newstring2 = "-".join(alist)   # join with linking character
print(newstring2)
