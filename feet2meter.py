def main():
    v = feet2meter(input("Сколько футов:"))
    print("Это будет", v, "метров.")

def feet2meter(v):
    v=v.strip("ft ")
    v=round(float(v)*0.3048, 2)
    return(v)

main()
