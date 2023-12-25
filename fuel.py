che=0
while(che!=1):
    try:
        z=input("Дробь: ")
        z=z.split("/")
        x=int(z[0])
        y=int(z[1])
        f=x/y
        if f <= 1:
            break

    except (ValueError, ZeroDivisionError):
        pass

f=round(f*100)
if(f>=99):
    print("F")
elif(f<=1):
    print("E")
else:
    print(str(f)+"%")
