try:
    import time as t
    print("type a word and this program will check if it is a palindrome or not ")
    print("\nExample:LOL is a Palindrome , NO is not a palindrome")
    z = 0
    y = ''
    x = str(input("Type a Word:")).lower()
    for i in x:
        y = y + (x[-1 - z])
        print(y)
        print(x[z]) 
        z += 1

    print(y)

    if y == x:
        t.sleep(1)
        print("According to my calculations")
        t.sleep(1)
        print("The word is!")
        t.sleep(1)
        print("A PALINDROME!!")
        input("Press Enter to Exit")
    else:
        t.sleep(1)
        print("According to my calculations")
        t.sleep(1)
        print("The word is!")
        t.sleep(1)
        print("not a palindrome Bruh ..")
        t.sleep(1)
        print("...")
        t.sleep(2)
        print("thats dissapointing ...")
        t.sleep(1)
        input("Anyways? Press Enter to Exit")
except Exception as e:
    print(e)
    input("Press enter to continue")




        