rain=str(input("Raining? (Yes/no): "))
temp=int(input("Temp:"))
if rain=="Yes" and temp<50:
    print("Wear a coat. Also, bring an umbrella.")
elif temp<50:
    print("Wear a coat.")
elif rain=="Yes":
    print("Bring an umbrella.")
else:
    print("Light clothing will be okay.")
