a = int(input("zadaj cislo a:"))
b = int(input("zadaj cislo b:"))
c = int(input("zadaj cislo c:"))
if a > b and a > c and b > c:
    if b>c:
        print(a,b,c)
    else:
        print(a,c,b)
elif b>a and b>c:
    if a>c:
        print(b,a,c)
    else:
        print(b,c,a)
elif c>a and c>b:
    if c>b:
        print(a,c,b)
    else:
        print(a,b,c)

