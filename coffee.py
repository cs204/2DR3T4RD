cof=0
while(cof<50):
    print("Нужная сумма:",50-cof)
    coin=int(input("Вставьте монету: "))
    if((coin==5) or (coin==10) or (coin==20) or (coin==50)):
        cof+=coin
print("Ваша сдача:",cof-50)
