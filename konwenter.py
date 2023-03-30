a=input("wybierz jednostkę którą przekształcasz (m, cm, mm, km,   m2, cm2, mm2, km2,   m3, cm3, mm3, km3  ): ")
b=input("wybierz jednostkę którą chcesz otrzymac(m, cm, mm, km,   m2, cm2, mm2, km2,   m3, cm3, mm3, km3  ): ")
c=float(input("podaj wartość: "))
while c<0:
    print("podaj liczbę nieujemną")
    break
    if a=="m" and b=="m":
        print("", c,"m")
    elif a=="m" and b=="cm":
        print("",c*100,"cm")
    elif a=="m" and b=="mm":
        print("",c*1000,"mm")
    elif a=="m" and b=="km":
        print("",c/1000,"km")

    elif a=="km" and b=="m":
        print("",c*1000,"m")
    elif a=="km" and b=="cm":
        print("",c*100000,"cm")
    elif a=="km" and b=="mm":
        print("",c*100,"mm")
    elif a=="km" and b=="km":
        print("",c,"km")

    elif a=="cm" and b=="cm":
        print("",c,"cm")
    elif a=="cm" and b=="m":
        print(c/100,"m")
    elif a=="cm" and b=="km":
        print(c/100000,"km")
    elif a=="cm" and b=="mm":
        print(c*10,"mm")

    elif a=="mm" and b=="mm":
        print(c,"mm")
    elif a=="mm" and b=="cm":
        print(c/10,"cm")
    elif a=="mm" and b=="m":
        print(c/1000,"m")
    elif a=="mm" and b=="km":
        print(c/1000000,"km")


    elif a=="mm2" and b=="mm2":
        print(c,"mm2")
    elif a=="mm2" and b=="cm2":
        print(c/100,"cm2")
    elif a=="mm2" and b=="m2":
        print(c/1000000,"m2")
    elif a=="mm2" and b=="km2":
        print(c/1000000000000,"km2")


    elif a=="cm2" and b=="mm2":
        print(c*100,"mm2")
    elif a=="cm2" and b=="cm2":
        print(c,"cm2")
    elif a=="cm2" and b=="m2":
        print(c/10000,"m2")
    elif a=="cm2" and b=="km2":
        print(c/10000000000,"km2")

    elif a=="m2" and b=="mm2":
        print(c*1000000,"mm2")
    elif a=="m2" and b=="cm2":
        print(c*10000,"cm2")
    elif a=="m2" and b=="m2":
        print(c,"m2")
    elif a=="m2" and b=="km2":
        print(c/1000000,"km2")

    elif a=="km2" and b=="mm2":
        print(c*1000000000000,"mm2")
    elif a=="km2" and b=="cm2":
        print(c*10000000000,"cm2")
    elif a=="km2" and b=="m2":
        print(c*1000000,"m2")
    elif a=="km2" and b=="km2":
        print(c,"km2")


    elif a=="km3" and b=="mm3":
        print(c*1000000000000000000,"mm3")
    elif a=="km3" and b=="cm3":
        print(c*1000000000000000,"cm3")
    elif a=="km3" and b=="m3":
        print(c*1000000000,"m3")
    elif a=="km3" and b=="km3":
        print(c,"km3")

    elif a=="m3" and b=="mm3":
        print(c*1000000000,"mm3")
    elif a=="m3" and b=="cm3":
        print(c*1000000,"cm3")
    elif a=="m3" and b=="m3":
        print(c,"m3")
    elif a=="m3" and b=="km3":
        print(c/1000000000,"km3")

    elif a=="cm3" and b=="mm3":
        print(c*1000,"mm3")
    elif a=="cm3" and b=="cm3":
        print(c,"cm3")
    elif a=="cm3" and b=="m3":
        print(c/1000000,"m3")
    elif a=="cm3" and b=="km3":
        print(c/1000000000000000,"km3")

    elif a=="mm3" and b=="mm3":
        print(c,"mm3")
    elif a=="mm3" and b=="cm3":
        print(c/1000,"cm3")
    elif a=="mm3" and b=="m3":
        print(c/1000000000,"m3")
    elif a=="mm3" and b=="km3":
        print(c/1000000000000000000,"km3")
else:
    print("wybieraj wśród PODANYCH jednostek")