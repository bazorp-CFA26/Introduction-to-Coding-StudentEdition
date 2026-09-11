temp=int(input("Input Tempature: "))
rain=str(input("Is It Raining? (Yes/No) "))
if rain=="yes" and temp<=60:
    print("Wear a coat and bring an umbralla bruh")
elif rain=="yes" and temp>60:
    print ("Bring an umbrella!")
elif rain=="no" and temp<=60:
    print("Wear a coat!")
else:
    print("Ah. Your fine. Wear light clothing.")
