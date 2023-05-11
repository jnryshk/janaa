masa=float(input("podaj swoją masę ciała (kg): "))
wzrost=float(input("podaj wzrost (m): "))

BMI=masa/(wzrost*wzrost)
print("twój bmi wynosi: ",'%.2f'%BMI,)

if BMI<18.5:
    while masa<0 and wzrost<0:
        print("podaj dodatnie wartości")
    print(  ''' twój BMI wskazuje na to ze masz niedowagę. 
    Przyczyną niedowagi jest długotrwale utrzymujący się ujemny bilans energetyczny związany np.
    z chorobą lub stosowaniem restrykcyjnej diety.
    Skutkiem zbyt małej wagi jestem.in. osłabienie, apatia, skłonność do infekcji''')
elif BMI >= 18.5 and BMI <25 :
    while masa<0 and wzrost<0:
        print("podaj dodatnie wartości")
    print( BMI, ''' masz prawidówą wagę, nie ma o co się martwić
          zachowuj zdrowy tryb życia ''')
elif BMI >=25 and BMI < 30:
    while masa<0 and wzrost<0:
        print("podaj dodatnie wartości")
    print ( ''' twój BMI wskazuje na to ze masz nadwagę.
    Lekarze zwracają uwagę na konieczność przestrzegania 
    zasad ograniczających ryzyko wystąpienia nadwagi i otyłości.''')
elif BMI >=30 and BMI < 35:
    while masa<0 and wzrost<0:
        print(" podaj dodatnie wartości")
    print(  ''' twój BMI wskazuje na to ze masz 1 stopień otyłości.
    W leczeniu dominują zmiana nawyków 
    żywieniowych oraz włączenie aktywności fizycznej, 
    które mają za zadanie skutecznie obniżyć masę ciała. ''')
elif BMI >=35 and BMI <40 :
    while masa<0 and wzrost<0:
        print("podaj dodatnie wartości")
    print(''' twój BMI wskazuje na to ze masz 2 stopień otyłości.
    Na początku leczenie polega na 
    zmianie diety i wdrożeniu aktywności fizycznej.''')
elif BMI >=40 :
    while masa<0 and wzrost<0:
        print("podaj dodatnie wartości")
    print( ''' twój BMI wskazuje na to ze masz 3 stopień otyłości.
    Otyłość olbrzymia zawsze wymaga interwencji chirurgicznej.''')
a=wzrost*wzrost*18.5 
b=wzrost*wzrost*25 
print("twoja prawidłowa waga: " '%.2f'%a "kg - " ,'%.2f'%b "kg")