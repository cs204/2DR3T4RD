cs=input("Верблюжий стиль: ")
zs=""
for b in cs:
    if (b.isupper()):
        zs+="_"+b.lower()
    else:
        zs+=b
print(zs)
