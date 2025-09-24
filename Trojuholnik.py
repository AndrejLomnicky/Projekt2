#obsah,taznice,uhly,objem,
import math
a=int(input("zadaj mi stranu a"))
b=int(input("zadaj mi stranu b"))
c=int(input("zadaj mi stranu c"))
#testujem ci je to trojuholnik
if (a+b>c) and (a+c>b)and (b+c>a):
    print("je to trojuholnik")
    #testujem ci je to pravouhly trojuholnik
if (a**2+b**2==c**2) or (a**2+c**2==b**2) or (b**2+c**2==a**2):
    print("je to pravouhly trojuholnik")
    o = (a+b+c)
    po= o/2
    S=(po*(po-a)*(po-b)*(po-c)))**0.5
    va = 2*S/a
    vb=2*Sb
    vc=2*Sc
    p_vpis=S/po
    p_opis1=(a*b*c)/(4*S)
            #pocitam uhly
     alpha = round(math.degrees(math.acos((b**2+c**2-a**2)/(2*b*c))),2)
     beta = round(math.degrees(math.acos((a**2+c**2-b**2)/(2*a*c))),2)
     gama = round(math.degrees(math.acos((a**2+b**2-c**2)/(2*b*c))),2)
print("obvod je:",o,"obsah je:",S,"po je:",po,"vyska na stranu va je:",va,)




