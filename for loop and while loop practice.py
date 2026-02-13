#!/usr/bin/env python3

letter = "abcdefghijklmnopqrstuvwxyz"
lemma = str(input("Please enter a letter :")).lower()

def lemman():
    for x in lemma:
        if x in "aeiou":
            print("This is a vowel.")
            gg = input("Do you want to try again? Please say 'yes' or 'no' to continue.").lower()
            if gg == "yes":
                return True
            else:
                exit()
        elif x in letter:
            print("This is a consonant.")
            gg = input("Do you want to try again? Please say 'yes' or 'no' to continue.").lower()
            if gg == "yes":
                return True
            else:
                exit()

        else:
            print("This is NOT a letter.")
            return True
    
lemman()

while True:
    lemma = str(input("Please enter a letter :")).lower()
    lemman()



        


    
    