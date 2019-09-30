names = ["H", "He", "Li", "Be"]

masses = [1.008, 4.003, 6.941, 9.012]

Dict2 = {}

for i in range(len(names)):
    Dict2[names[i]] = masses[i]

print(Dict2)
print(Dict2["He"])
print(Dict2["H"])
print(Dict2["Li"])
print(Dict2["Be"])
print("Li" in Dict2)
print("H" in Dict2)
print("Que onda" in Dict2)
print("O" in Dict2)
