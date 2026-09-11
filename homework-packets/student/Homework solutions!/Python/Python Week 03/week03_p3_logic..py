age=int(input("How old are you? "))
answer1=str(input("Do you have a admission token? "))
if age>13 and answer1 == "yes":
    print ("The gate has opened. Proceed.")
if age<13 or answer1 == "no":
    print ("DENIED.")
