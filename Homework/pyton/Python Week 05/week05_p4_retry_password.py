password="KanYe"
while True:
    guess= str(input("Input Password: "))
    if guess==password:
        print ("Correct Password. Logging in...")
        break
    print ("INCORRECT. TRY AGAIN.")