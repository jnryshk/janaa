import math

figura=input("podaj jedną z podanych figur :prostokąt, trójkąt, równoległobok, romb, trapez, koło: ")
if figura == "prostokąt":
    a=float(input("podaj długość pierwszego boku:  "))
    b=float(input("podaj długość drugiego boku: "))
    while a<=0 or b<=0:
         print("podaj liczby dodatnie")
         a=float(input("podaj długość pierwszego boku:  "))
         b=float(input("podaj długość drugiego boku: "))
    pole=a*b
    print("pole twojego prostokątu to: " , pole )

elif figura=="trójkąt":
    a=float(input("podaj długość podstawy trojkątu: "))
    h=float(input("podaj wysokość trójkątu: "))
    while a<=0 or h<=0:
        print("podaj wartości dodatnie")
        a=float(input("podaj długość podstawy trojkątu: "))
        h=float(input("podaj wysokość trójkątu: "))
    pole1=0.5*a*h
    print("pole twojego trójkątu to: " , pole1)

elif figura=="równoległobok":
    a=float(input("podaj dlugość boku: "))
    h=float(input("podaj wysokość: "))
    while a<=0 or h<=0:
        print("podaj liczby dodatnie")
        a=float(input("podaj dlugość boku: "))
        h=float(input("podaj wysokość: "))
    pole2=a*h
    print("pole twojego trójkątu to: " , pole2)
elif figura=="romb":
    e=float(input("podaj dlugość pierwszej przekątnej:  "))
    f=float(input("podaj dlugość pierwszej przekątnej:  "))
    while e<=0 or f<=0:
         print("podaj liczby dodatnie")
         e=float(input("podaj dlugość pierwszej przekątnej:  "))
         f=float(input("podaj dlugość pierwszej przekątnej:  "))
    pole3=0.5*e*f
    print("pole twojego trójkątu to: " , pole3)
   
elif figura=="trapez":
    a=float(input("podaj dlugość górnego boku trapezu: "))
    b=float(input("podaj dlugość dolnego boku trapezu: "))
    h=float(input("podaj wysokość trapezu: "))
    c=a+b
    while a<=0 or b<=0 or h<=0:
        print("podaj liczby dodatnie")
        a=float(input("podaj dlugość górnego boku trapezu: "))
        b=float(input("podaj dlugość dolnego boku trapezu: "))
        h=float(input("podaj wysokość trapezu: "))
    pole4=0.5*c*h
    print("pole twojego trapezu to: " , pole4)
   
elif figura=="koło":
    r=float(input("podaj promień koła: "))
    while r<=0 :
        print("podaj liczby dodatnie")
        r=float(input("podaj promień koła: "))
    pole5=r**2*math.pi
    print("pole twojego kołą to: " , pole5) 
    