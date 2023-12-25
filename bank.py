s=input("Приветствие: ")
s=s.lower()
if(s.startswith("з")):
    if(s.startswith("здравствуйте")):
        print("$0")
    else:
        print("$20")
else:
    print("$100")
