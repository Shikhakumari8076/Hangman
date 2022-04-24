import random
print("!**___welcome to our Game Hangman___**!")
print("-----------------------------------------------!!")

worddictionary=["important","nobody","handle","hostel","live","life"]
### chose a random word

randomword = random.choice(worddictionary)
for x in randomword:
    print("_",end=" ")
    
def print_hangman(wrong):
    if (wrong==0):
        print("\n+---+")
        print("    |")
        print("    |")
        print("    |")
        print("   ===")
    elif(wrong==1):
        print("\n+---+")
        print("  0  |")
        print("     |")
        print("     |")
        print("   ===")
    elif(wrong==2):
        print("\n+---+")
        print("  0  |")
        print("  |  |")
        print("     |")
        print("   ===")
    elif(wrong==3):
        print("\n+---+")
        print("  0  |")
        print(" /|   ")
        print("     |")
        print("   ===")
    elif(wrong==4):
        print("\n+---+")
        print("  0  |")
        print(" /|\ |")
        print("     |")
        print("   ===")
    elif (wrong==5):
        print("\n+---+")
        print("  0  |")
        print(" /|\ |")
        print("  |  |")
        print("   ===")
    elif(wrong==7):
        print("\n+---+")
        print("  0  |")
        print(" /|\ |")
        print("  |")
        print(" /|")
        print("   ===")
    elif(wrong==8):
        print("\n+---+")
        print("  0  |")
        print(" /|\ |")
        print("  | ")
        print(" /| ")
        print(" /|\ ")
        print("   ===")

def printword(guessdletters):
    counter=0
    rightletters=0
    for char in randomword:
        if (char in guessdletters):
            print(randomword[counter],end=" ")
            rightletters+=1
        else:
            print(" ",end=" ")
        counter+=1
    return rightletters

def printlines():
    print("\r")
    for char in randomword:
        print("\u203E",end=" ")

length_of_word_guess =len(randomword)
amount_of_times_wrong =0
current_guess_index =0
current_letters_guessed =[]
current_leters_right =0

while(amount_of_times_wrong != 6 and current_leters_right != length_of_word_guess):
    print("\nletters guessed so far:")
    for  letter in current_letters_guessed:
        print(letter,end=" ") 
    ### prompt user for input

    
    letterguessed =input("\nguess a letter:")
    ### user is right

    if(randomword[current_guess_index]==letterguessed):
        print_hangman(amount_of_times_wrong)
        ### print word

        current_guess_index+=1
        current_letters_guessed.append(letterguessed)
        current_leters_right = printword(current_letters_guessed)
        printlines()
    ### user was wrong af

    else:
        amount_of_times_wrong+=1
        current_letters_guessed.append(letterguessed)
        ### update the drawing

        print_hangman(amount_of_times_wrong)
        ### print word
        current_leters_right = printword(current_letters_guessed)
        printlines()
print("**___Game is over___**")
print("____well played____")
print("----THANK YOU----")






 