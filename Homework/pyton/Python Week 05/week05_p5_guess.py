supadupasecretnumber= 9
while True:
    guess=int(input("Input: "))
    if guess < supadupasecretnumber:
        print ("Too Low.")
    if guess > supadupasecretnumber:
        print ("Too high.")
    if guess==supadupasecretnumber:
        print ("Correct.")
        break
