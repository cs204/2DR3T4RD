def convert(x):
    s=x
    n=s.replace(":)","\U0001F642")
    m=n.replace(":(","\U0001F641")
    return(m)

def main():
    y=input()
    z=convert(y)
    print(z)

main()
