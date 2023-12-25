menu={"кофе": 20.00,"чай": 10.00,"булочка": 5.00,"салат": 30.40,"пирожное": 45.50}
total=0
while(True):
    try:
        s=input("Блюдо: ")
        for i in menu:
            if i==s:
                total+=menu[i]
    except EOFError:
        break
print("\nСумма:",str(round(total,1))+"0")
