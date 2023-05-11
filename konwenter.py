a=input("wybierz jednostkę którą przekształcasz (m, cm, mm, km,   m2, cm2, mm2, km2,   m3, cm3, mm3, km3  ): ")
b=input("wybierz jednostkę którą chcesz otrzymac(m, cm, mm, km,   m2, cm2, mm2, km2,   m3, cm3, mm3, km3  ): ")
c=float(input("podaj wartość: "))

if a=="m" and b=="m":
        while c<0:
                print("podaj wartosć dodatnią")
                a=input("wybierz jednostkę którą przekształcasz (m, cm, mm, km,   m2, cm2, mm2, km2,   m3, cm3, mm3, km3  ): ")
                b=input("wybierz jednostkę którą chcesz otrzymac(m, cm, mm, km,   m2, cm2, mm2, km2,   m3, cm3, mm3, km3  ): ")
                c=float(input("podaj wartość: "))
        print("", c,"m")
elif a=="m" and b=="cm":
        while c<0:
                print("podaj wartosć dodatnią")
                a=input("wybierz jednostkę którą przekształcasz (m, cm, mm, km,   m2, cm2, mm2, km2,   m3, cm3, mm3, km3  ): ")
                b=input("wybierz jednostkę którą chcesz otrzymac(m, cm, mm, km,   m2, cm2, mm2, km2,   m3, cm3, mm3, km3  ): ")
                c=float(input("podaj wartość: "))
        print("",c*100,"cm")
elif a=="m" and b=="mm":
        while c<0:
                print("podaj wartosć dodatnią")
                a=input("wybierz jednostkę którą przekształcasz (m, cm, mm, km,   m2, cm2, mm2, km2,   m3, cm3, mm3, km3  ): ")
                b=input("wybierz jednostkę którą chcesz otrzymac(m, cm, mm, km,   m2, cm2, mm2, km2,   m3, cm3, mm3, km3  ): ")
                c=float(input("podaj wartość: "))
        print("",c*1000,"mm")
elif a=="m" and b=="km":
        while c<0:
                print("podaj wartosć dodatnią")
                a=input("wybierz jednostkę którą przekształcasz (m, cm, mm, km,   m2, cm2, mm2, km2,   m3, cm3, mm3, km3  ): ")
                b=input("wybierz jednostkę którą chcesz otrzymac(m, cm, mm, km,   m2, cm2, mm2, km2,   m3, cm3, mm3, km3  ): ")
                c=float(input("podaj wartość: "))
        print("",c/1000,"km")

elif a=="km" and b=="m":
        while c<0:
                print("podaj wartosć dodatnią")
                a=input("wybierz jednostkę którą przekształcasz (m, cm, mm, km,   m2, cm2, mm2, km2,   m3, cm3, mm3, km3  ): ")
                b=input("wybierz jednostkę którą chcesz otrzymac(m, cm, mm, km,   m2, cm2, mm2, km2,   m3, cm3, mm3, km3  ): ")
                c=float(input("podaj wartość: "))
        print("",c*1000,"m")
elif a=="km" and b=="cm":
        while c<0:
                print("podaj wartosć dodatnią")
                a=input("wybierz jednostkę którą przekształcasz (m, cm, mm, km,   m2, cm2, mm2, km2,   m3, cm3, mm3, km3  ): ")
                b=input("wybierz jednostkę którą chcesz otrzymac(m, cm, mm, km,   m2, cm2, mm2, km2,   m3, cm3, mm3, km3  ): ")
                c=float(input("podaj wartość: "))
        print("",c*100000,"cm")
elif a=="km" and b=="mm":
        while c<0:
                print("podaj wartosć dodatnią")
                a=input("wybierz jednostkę którą przekształcasz (m, cm, mm, km,   m2, cm2, mm2, km2,   m3, cm3, mm3, km3  ): ")
                b=input("wybierz jednostkę którą chcesz otrzymac(m, cm, mm, km,   m2, cm2, mm2, km2,   m3, cm3, mm3, km3  ): ")
                c=float(input("podaj wartość: "))
        print("",c*100,"mm")
elif a=="km" and b=="km":
        while c<0:
                print("podaj wartosć dodatnią")
                a=input("wybierz jednostkę którą przekształcasz (m, cm, mm, km,   m2, cm2, mm2, km2,   m3, cm3, mm3, km3  ): ")
                b=input("wybierz jednostkę którą chcesz otrzymac(m, cm, mm, km,   m2, cm2, mm2, km2,   m3, cm3, mm3, km3  ): ")
                c=float(input("podaj wartość: "))
        print("",c,"km")

elif a=="cm" and b=="cm":
        while c<0:
                print("podaj wartosć dodatnią")
                a=input("wybierz jednostkę którą przekształcasz (m, cm, mm, km,   m2, cm2, mm2, km2,   m3, cm3, mm3, km3  ): ")
                b=input("wybierz jednostkę którą chcesz otrzymac(m, cm, mm, km,   m2, cm2, mm2, km2,   m3, cm3, mm3, km3  ): ")
                c=float(input("podaj wartość: "))
        print("",c,"cm")
elif a=="cm" and b=="m":
        while c<0:
                print("podaj wartosć dodatnią")
                a=input("wybierz jednostkę którą przekształcasz (m, cm, mm, km,   m2, cm2, mm2, km2,   m3, cm3, mm3, km3  ): ")
                b=input("wybierz jednostkę którą chcesz otrzymac(m, cm, mm, km,   m2, cm2, mm2, km2,   m3, cm3, mm3, km3  ): ")
                c=float(input("podaj wartość: "))
        print(c/100,"m")
elif a=="cm" and b=="km":
        while c<0:
                print("podaj wartosć dodatnią")
                a=input("wybierz jednostkę którą przekształcasz (m, cm, mm, km,   m2, cm2, mm2, km2,   m3, cm3, mm3, km3  ): ")
                b=input("wybierz jednostkę którą chcesz otrzymac(m, cm, mm, km,   m2, cm2, mm2, km2,   m3, cm3, mm3, km3  ): ")
                c=float(input("podaj wartość: "))
        print(c/100000,"km")
elif a=="cm" and b=="mm":
        while c<0:
                print("podaj wartosć dodatnią")
                a=input("wybierz jednostkę którą przekształcasz (m, cm, mm, km,   m2, cm2, mm2, km2,   m3, cm3, mm3, km3  ): ")
                b=input("wybierz jednostkę którą chcesz otrzymac(m, cm, mm, km,   m2, cm2, mm2, km2,   m3, cm3, mm3, km3  ): ")
                c=float(input("podaj wartość: "))
        print(c*10,"mm")

elif a=="mm" and b=="mm":
        while c<0:
                print("podaj wartosć dodatnią")
                a=input("wybierz jednostkę którą przekształcasz (m, cm, mm, km,   m2, cm2, mm2, km2,   m3, cm3, mm3, km3  ): ")
                b=input("wybierz jednostkę którą chcesz otrzymac(m, cm, mm, km,   m2, cm2, mm2, km2,   m3, cm3, mm3, km3  ): ")
                c=float(input("podaj wartość: "))
        print(c,"mm")
elif a=="mm" and b=="cm":
        while c<0:
                print("podaj wartosć dodatnią")
                a=input("wybierz jednostkę którą przekształcasz (m, cm, mm, km,   m2, cm2, mm2, km2,   m3, cm3, mm3, km3  ): ")
                b=input("wybierz jednostkę którą chcesz otrzymac(m, cm, mm, km,   m2, cm2, mm2, km2,   m3, cm3, mm3, km3  ): ")
                c=float(input("podaj wartość: "))
        print(c/10,"cm")
elif a=="mm" and b=="km":
        while c<0:
                print("podaj wartosć dodatnią")
                a=input("wybierz jednostkę którą przekształcasz (m, cm, mm, km,   m2, cm2, mm2, km2,   m3, cm3, mm3, km3  ): ")
                b=input("wybierz jednostkę którą chcesz otrzymac(m, cm, mm, km,   m2, cm2, mm2, km2,   m3, cm3, mm3, km3  ): ")
                c=float(input("podaj wartość: "))
        print(c/1000000,"km")
elif a=="mm" and b=="m":
        while c<0:
                print("podaj wartosć dodatnią")
                a=input("wybierz jednostkę którą przekształcasz (m, cm, mm, km,   m2, cm2, mm2, km2,   m3, cm3, mm3, km3  ): ")
                b=input("wybierz jednostkę którą chcesz otrzymac(m, cm, mm, km,   m2, cm2, mm2, km2,   m3, cm3, mm3, km3  ): ")
                c=float(input("podaj wartość: ")) 
        print(c/1000,"km") 


elif a=="mm2" and b=="mm2":
        while c<0:
                print("podaj wartosć dodatnią")
                a=input("wybierz jednostkę którą przekształcasz (m, cm, mm, km,   m2, cm2, mm2, km2,   m3, cm3, mm3, km3  ): ")
                b=input("wybierz jednostkę którą chcesz otrzymac(m, cm, mm, km,   m2, cm2, mm2, km2,   m3, cm3, mm3, km3  ): ")
                c=float(input("podaj wartość: "))
        print(c,"mm2")
elif a=="mm2" and b=="cm2":
        while c<0:
                print("podaj wartosć dodatnią")
                a=input("wybierz jednostkę którą przekształcasz (m, cm, mm, km,   m2, cm2, mm2, km2,   m3, cm3, mm3, km3  ): ")
                b=input("wybierz jednostkę którą chcesz otrzymac(m, cm, mm, km,   m2, cm2, mm2, km2,   m3, cm3, mm3, km3  ): ")
                c=float(input("podaj wartość: "))
        print(c/100,"cm2")
elif a=="mm2" and b=="m2":
        while c<0:
                print("podaj wartosć dodatnią")
                a=input("wybierz jednostkę którą przekształcasz (m, cm, mm, km,   m2, cm2, mm2, km2,   m3, cm3, mm3, km3  ): ")
                b=input("wybierz jednostkę którą chcesz otrzymac(m, cm, mm, km,   m2, cm2, mm2, km2,   m3, cm3, mm3, km3  ): ")
                c=float(input("podaj wartość: "))
        print(c/1000000,"m2")
elif a=="mm2" and b=="km2":
        while c<0:
                print("podaj wartosć dodatnią")
                a=input("wybierz jednostkę którą przekształcasz (m, cm, mm, km,   m2, cm2, mm2, km2,   m3, cm3, mm3, km3  ): ")
                b=input("wybierz jednostkę którą chcesz otrzymac(m, cm, mm, km,   m2, cm2, mm2, km2,   m3, cm3, mm3, km3  ): ")
                c=float(input("podaj wartość: "))
        print(c/1000000000000,"km2")


elif a=="cm2" and b=="mm2":
        while c<0:
                print("podaj wartosć dodatnią")
                a=input("wybierz jednostkę którą przekształcasz (m, cm, mm, km,   m2, cm2, mm2, km2,   m3, cm3, mm3, km3  ): ")
                b=input("wybierz jednostkę którą chcesz otrzymac(m, cm, mm, km,   m2, cm2, mm2, km2,   m3, cm3, mm3, km3  ): ")
                c=float(input("podaj wartość: "))
        print(c*100,"mm2")
elif a=="cm2" and b=="cm2":
        while c<0:
                print("podaj wartosć dodatnią")
                a=input("wybierz jednostkę którą przekształcasz (m, cm, mm, km,   m2, cm2, mm2, km2,   m3, cm3, mm3, km3  ): ")
                b=input("wybierz jednostkę którą chcesz otrzymac(m, cm, mm, km,   m2, cm2, mm2, km2,   m3, cm3, mm3, km3  ): ")
                c=float(input("podaj wartość: "))
        print(c,"cm2")
elif a=="cm2" and b=="m2":
        while c<0:
                print("podaj wartosć dodatnią")
                a=input("wybierz jednostkę którą przekształcasz (m, cm, mm, km,   m2, cm2, mm2, km2,   m3, cm3, mm3, km3  ): ")
                b=input("wybierz jednostkę którą chcesz otrzymac(m, cm, mm, km,   m2, cm2, mm2, km2,   m3, cm3, mm3, km3  ): ")
                c=float(input("podaj wartość: "))
        print(c/10000,"m2")
elif a=="cm2" and b=="km2":
        while c<0:
                print("podaj wartosć dodatnią")
                a=input("wybierz jednostkę którą przekształcasz (m, cm, mm, km,   m2, cm2, mm2, km2,   m3, cm3, mm3, km3  ): ")
                b=input("wybierz jednostkę którą chcesz otrzymac(m, cm, mm, km,   m2, cm2, mm2, km2,   m3, cm3, mm3, km3  ): ")
                c=float(input("podaj wartość: "))
        print(c/10000000000,"km2")

elif a=="m2" and b=="mm2":

        while c<0:
                print("podaj wartosć dodatnią")
                a=input("wybierz jednostkę którą przekształcasz (m, cm, mm, km,   m2, cm2, mm2, km2,   m3, cm3, mm3, km3  ): ")
                b=input("wybierz jednostkę którą chcesz otrzymac(m, cm, mm, km,   m2, cm2, mm2, km2,   m3, cm3, mm3, km3  ): ")
                c=float(input("podaj wartość: "))
        print(c*1000000,"mm2")
elif a=="m2" and b=="cm2":
        
        while c<0:
                print("podaj wartosć dodatnią")
                a=input("wybierz jednostkę którą przekształcasz (m, cm, mm, km,   m2, cm2, mm2, km2,   m3, cm3, mm3, km3  ): ")
                b=input("wybierz jednostkę którą chcesz otrzymac(m, cm, mm, km,   m2, cm2, mm2, km2,   m3, cm3, mm3, km3  ): ")
                c=float(input("podaj wartość: "))
        print(c*10000,"cm2")
elif a=="m2" and b=="m2":
        while c<0:
                print("podaj wartosć dodatnią")
                a=input("wybierz jednostkę którą przekształcasz (m, cm, mm, km,   m2, cm2, mm2, km2,   m3, cm3, mm3, km3  ): ")
                b=input("wybierz jednostkę którą chcesz otrzymac(m, cm, mm, km,   m2, cm2, mm2, km2,   m3, cm3, mm3, km3  ): ")
                c=float(input("podaj wartość: "))
        print(c,"m2")
elif a=="m2" and b=="km2":
        
        while c<0:
                print("podaj wartosć dodatnią")
                a=input("wybierz jednostkę którą przekształcasz (m, cm, mm, km,   m2, cm2, mm2, km2,   m3, cm3, mm3, km3  ): ")
                b=input("wybierz jednostkę którą chcesz otrzymac(m, cm, mm, km,   m2, cm2, mm2, km2,   m3, cm3, mm3, km3  ): ")
                c=float(input("podaj wartość: "))
        print(c/1000000,"km2")

elif a=="km2" and b=="mm2":
        while c<0:
                print("podaj wartosć dodatnią")
                a=input("wybierz jednostkę którą przekształcasz (m, cm, mm, km,   m2, cm2, mm2, km2,   m3, cm3, mm3, km3  ): ")
                b=input("wybierz jednostkę którą chcesz otrzymac(m, cm, mm, km,   m2, cm2, mm2, km2,   m3, cm3, mm3, km3  ): ")
                c=float(input("podaj wartość: "))
        print(c*1000000000000,"mm2")
elif a=="km2" and b=="cm2":
        while c<0:
                print("podaj wartosć dodatnią")
                a=input("wybierz jednostkę którą przekształcasz (m, cm, mm, km,   m2, cm2, mm2, km2,   m3, cm3, mm3, km3  ): ")
                b=input("wybierz jednostkę którą chcesz otrzymac(m, cm, mm, km,   m2, cm2, mm2, km2,   m3, cm3, mm3, km3  ): ")
                c=float(input("podaj wartość: "))
        print(c*10000000000,"cm2")
elif a=="km2" and b=="m2":
        while c<0:
                print("podaj wartosć dodatnią")
                a=input("wybierz jednostkę którą przekształcasz (m, cm, mm, km,   m2, cm2, mm2, km2,   m3, cm3, mm3, km3  ): ")
                b=input("wybierz jednostkę którą chcesz otrzymac(m, cm, mm, km,   m2, cm2, mm2, km2,   m3, cm3, mm3, km3  ): ")
                c=float(input("podaj wartość: "))
        print(c*1000000,"m2")
elif a=="km2" and b=="km2":
        while c<0:
                print("podaj wartosć dodatnią")
                a=input("wybierz jednostkę którą przekształcasz (m, cm, mm, km,   m2, cm2, mm2, km2,   m3, cm3, mm3, km3  ): ")
                b=input("wybierz jednostkę którą chcesz otrzymac(m, cm, mm, km,   m2, cm2, mm2, km2,   m3, cm3, mm3, km3  ): ")
                c=float(input("podaj wartość: "))
        print(c,"km2")

elif a=="km3" and b=="mm3":
        while c<0:
                print("podaj wartosć dodatnią")
                a=input("wybierz jednostkę którą przekształcasz (m, cm, mm, km,   m2, cm2, mm2, km2,   m3, cm3, mm3, km3  ): ")
                b=input("wybierz jednostkę którą chcesz otrzymac(m, cm, mm, km,   m2, cm2, mm2, km2,   m3, cm3, mm3, km3  ): ")
                c=float(input("podaj wartość: "))
        print(c*1000000000000000000,"mm3")
elif a=="km3" and b=="cm3":
        while c<0:
                print("podaj wartosć dodatnią")
                a=input("wybierz jednostkę którą przekształcasz (m, cm, mm, km,   m2, cm2, mm2, km2,   m3, cm3, mm3, km3  ): ")
                b=input("wybierz jednostkę którą chcesz otrzymac(m, cm, mm, km,   m2, cm2, mm2, km2,   m3, cm3, mm3, km3  ): ")
                c=float(input("podaj wartość: "))
        print(c*1000000000000000,"cm3")
elif a=="km3" and b=="m3":
        while c<0:
                print("podaj wartosć dodatnią")
                a=input("wybierz jednostkę którą przekształcasz (m, cm, mm, km,   m2, cm2, mm2, km2,   m3, cm3, mm3, km3  ): ")
                b=input("wybierz jednostkę którą chcesz otrzymac(m, cm, mm, km,   m2, cm2, mm2, km2,   m3, cm3, mm3, km3  ): ")
                c=float(input("podaj wartość: "))
        print(c*1000000000,"m3")
elif a=="km3" and b=="km3":
        while c<0:
                print("podaj wartosć dodatnią")
                a=input("wybierz jednostkę którą przekształcasz (m, cm, mm, km,   m2, cm2, mm2, km2,   m3, cm3, mm3, km3  ): ")
                b=input("wybierz jednostkę którą chcesz otrzymac(m, cm, mm, km,   m2, cm2, mm2, km2,   m3, cm3, mm3, km3  ): ")
                c=float(input("podaj wartość: "))
        print(c,"km3")

elif a=="m3" and b=="mm3":
        while c<0:
                print("podaj wartosć dodatnią")
                a=input("wybierz jednostkę którą przekształcasz (m, cm, mm, km,   m2, cm2, mm2, km2,   m3, cm3, mm3, km3  ): ")
                b=input("wybierz jednostkę którą chcesz otrzymac(m, cm, mm, km,   m2, cm2, mm2, km2,   m3, cm3, mm3, km3  ): ")
                c=float(input("podaj wartość: "))
        print(c*1000000000,"mm3")
elif a=="m3" and b=="cm3":
        while c<0:
                print("podaj wartosć dodatnią")
                a=input("wybierz jednostkę którą przekształcasz (m, cm, mm, km,   m2, cm2, mm2, km2,   m3, cm3, mm3, km3  ): ")
                b=input("wybierz jednostkę którą chcesz otrzymac(m, cm, mm, km,   m2, cm2, mm2, km2,   m3, cm3, mm3, km3  ): ")
                c=float(input("podaj wartość: "))
        print(c*1000000,"cm3")
elif a=="m3" and b=="m3":
        while c<0:
                print("podaj wartosć dodatnią")
                a=input("wybierz jednostkę którą przekształcasz (m, cm, mm, km,   m2, cm2, mm2, km2,   m3, cm3, mm3, km3  ): ")
                b=input("wybierz jednostkę którą chcesz otrzymac(m, cm, mm, km,   m2, cm2, mm2, km2,   m3, cm3, mm3, km3  ): ")
                c=float(input("podaj wartość: "))
        print(c,"m3")
elif a=="m3" and b=="km3":
        while c<0:
                print("podaj wartosć dodatnią")
                a=input("wybierz jednostkę którą przekształcasz (m, cm, mm, km,   m2, cm2, mm2, km2,   m3, cm3, mm3, km3  ): ")
                b=input("wybierz jednostkę którą chcesz otrzymac(m, cm, mm, km,   m2, cm2, mm2, km2,   m3, cm3, mm3, km3  ): ")
                c=float(input("podaj wartość: "))
        print(c/1000000000,"km3")

elif a=="cm3" and b=="mm3":
        while c<0:
                print("podaj wartosć dodatnią")
                a=input("wybierz jednostkę którą przekształcasz (m, cm, mm, km,   m2, cm2, mm2, km2,   m3, cm3, mm3, km3  ): ")
                b=input("wybierz jednostkę którą chcesz otrzymac(m, cm, mm, km,   m2, cm2, mm2, km2,   m3, cm3, mm3, km3  ): ")
                c=float(input("podaj wartość: "))
        print(c*1000,"mm3")
elif a=="cm3" and b=="cm3":
        while c<0:
                print("podaj wartosć dodatnią")
                a=input("wybierz jednostkę którą przekształcasz (m, cm, mm, km,   m2, cm2, mm2, km2,   m3, cm3, mm3, km3  ): ")
                b=input("wybierz jednostkę którą chcesz otrzymac(m, cm, mm, km,   m2, cm2, mm2, km2,   m3, cm3, mm3, km3  ): ")
                c=float(input("podaj wartość: "))
        print(c,"cm3")
elif a=="cm3" and b=="m3":
        while c<0:
                print("podaj wartosć dodatnią")
                a=input("wybierz jednostkę którą przekształcasz (m, cm, mm, km,   m2, cm2, mm2, km2,   m3, cm3, mm3, km3  ): ")
                b=input("wybierz jednostkę którą chcesz otrzymac(m, cm, mm, km,   m2, cm2, mm2, km2,   m3, cm3, mm3, km3  ): ")
                c=float(input("podaj wartość: "))
        print(c/1000000,"m3")
elif a=="cm3" and b=="km3":
        while c<0:
                print("podaj wartosć dodatnią")
                a=input("wybierz jednostkę którą przekształcasz (m, cm, mm, km,   m2, cm2, mm2, km2,   m3, cm3, mm3, km3  ): ")
                b=input("wybierz jednostkę którą chcesz otrzymac(m, cm, mm, km,   m2, cm2, mm2, km2,   m3, cm3, mm3, km3  ): ")
                c=float(input("podaj wartość: "))
        print(c/1000000000000000,"km3")

elif a=="mm3" and b=="mm3":
        while c<0:
                print("podaj wartosć dodatnią")
                a=input("wybierz jednostkę którą przekształcasz (m, cm, mm, km,   m2, cm2, mm2, km2,   m3, cm3, mm3, km3  ): ")
                b=input("wybierz jednostkę którą chcesz otrzymac(m, cm, mm, km,   m2, cm2, mm2, km2,   m3, cm3, mm3, km3  ): ")
                c=float(input("podaj wartość: "))
        print(c,"mm3")
elif a=="mm3" and b=="cm3":
        while c<0:
                print("podaj wartosć dodatnią")
                a=input("wybierz jednostkę którą przekształcasz (m, cm, mm, km,   m2, cm2, mm2, km2,   m3, cm3, mm3, km3  ): ")
                b=input("wybierz jednostkę którą chcesz otrzymac(m, cm, mm, km,   m2, cm2, mm2, km2,   m3, cm3, mm3, km3  ): ")
                c=float(input("podaj wartość: "))
        print(c/1000,"cm3")
elif a=="mm3" and b=="m3":
        while c<0:
                print("podaj wartosć dodatnią")
                a=input("wybierz jednostkę którą przekształcasz (m, cm, mm, km,   m2, cm2, mm2, km2,   m3, cm3, mm3, km3  ): ")
                b=input("wybierz jednostkę którą chcesz otrzymac(m, cm, mm, km,   m2, cm2, mm2, km2,   m3, cm3, mm3, km3  ): ")
                c=float(input("podaj wartość: "))
        print(c/1000000000,"m3")
elif a=="mm3" and b=="km3":
        while c<0:
                print("podaj wartosć dodatnią")
                a=input("wybierz jednostkę którą przekształcasz (m, cm, mm, km,   m2, cm2, mm2, km2,   m3, cm3, mm3, km3  ): ")
                b=input("wybierz jednostkę którą chcesz otrzymac(m, cm, mm, km,   m2, cm2, mm2, km2,   m3, cm3, mm3, km3  ): ")
                c=float(input("podaj wartość: "))
        print(c/1000000000000000000,"km3")
else:
        print("wybieraj wśród PODANYCH jednostek i pamietaj ze nie da sie przekształcić np jednostek kwadratowych na zwykłe i td")