
def checkPalindrome(word):
    #reverses the word
    word = word.lower()
    
    #takes out all special characters
    word = word.replace(" ", "")
    word = word.replace(":", "")
    word = word.replace(".","")
    word = word.replace("!","")
    word = word.replace("?","")
    word = word.replace(",","")
    word = word.replace("'","")
    
    #reverses the string    
    checkPal = word[::-1]

    #compare the string to the reverse string
    if checkPal == word:
        return True
    else:
        return False 

print("Type EXIT to stop.")
while True:
    pt_pal = input("Please enter a string: ")
    if pt_pal == "EXIT":
        print("Thanks for using my program! Goodbye.")
        break
    elif len(pt_pal) <= 2:
        print("String too short. Try again.")
    else:
        if checkPalindrome(pt_pal): 
            print("This string <",pt_pal,"> is a palindrome!")
        else:
            print("This string <",pt_pal,"> is not a palindrome.")




        
        

