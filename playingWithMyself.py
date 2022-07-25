# -*- coding: utf-8 -*-
"""
Created on Fri Jul  1 11:30:33 2022

@author: byteandpeaces@gmail.com
"""


def fiveLetterWordList():
  """ 
Reads in the list of five letter words from a .txt and stores them as the 
solution words to test the program with as well as the the initial list of 
potential guesses
  """
#-Reading in list of five letter words that was prepared previously
  fiveLetterWords = list()
  with open("five_letter_list.txt", "r") as f:
    for line in f:
        fiveLetterWords.append(line.strip())
  f.close()

  return fiveLetterWords

# These can be (re)moved later when the rest of the program is flowing
solutionList = fiveLetterWordList()
firstGuess = "raise"



 #-----------------------------------------------------------------------------
    def get_correct_letters(user_guess):

        user_input = input("enter the position (1-5) of any letters that are in the word: ")
        in_word = user_input.split(",")
        if in_word[0] == "0": 
            in_word = list() # this ensures that a "0" as user input doesn't register as anything being correct
        for num in in_word: correct_letters.append(user_guess[int(num)-1])
        #print("Correct letters! ...I hope: ", correct_letters )
        
        for letter in user_guess:
            if letter not in correct_letters: incorrect_letters.append(letter)
        #print("incorrect letters: ", incorrect_letters)

        return correct_letters, incorrect_letters



#-----------------------------------------------------------------------------
    def get_incorrect_letters(user_guess, correct_letters):

       for letter in user_guess:
            if letter not in correct_letters and letter not in incorrect_letters: 
                incorrect_letters.append(letter)
            print("incorrect letters: ", incorrect_letters)

       return incorrect_letters




#-----------------------------------------------------------------------------
    def keep_correct(current_guesses, correct_letters):

        for word in current_guesses:
            word_letters = [char for char in word]
            test = all(x in word_letters for x in correct_letters)
            if test == True: new_guesses.append(word)
            word_letters = list()
        print(len(new_guesses), " at end of correct test")

        return new_guesses



#-----------------------------------------------------------------------------
    def remove_incorrect(current_guesses, incorrect_letters):

        for word in current_guesses:
            word_letters = [char for char in word]
            test = any(x in word_letters for x in incorrect_letters)
            if test == False: new_guesses.append(word)
            word_letters = list()
        print(len(new_guesses), " at end of incorrect test")

        return new_guesses



#------------------------------------------------------------------------------
    def position_check(current_guesses, user_guess):
        user_input = input("enter the position (1-5) of any letters that are in the correct position (green): ")        
        correct_pos = user_input.split(",")

        if correct_pos[0] == "0": 
            correct_pos = list() # this ensures that a "0" as user input doesn't register as anything being correct
            #print("correct_pos should be empty list: ", correct_pos)
        for possibility in current_guesses:
            error = False
            for num in correct_pos:
                if user_guess[int(num)-1] != possibility[int(num)-1]:
                    #print("error",num, type(num), user_guess[int(num)-1], possibility )
                    error = True

            for item in ["1","2","3","4","5"]:
                if item not in correct_pos and user_guess[int(item)-1] == possibility[int(item)-1]:
                    error = True
 
            if error == False: new_guesses.append(possibility)

        return new_guesses


#-----------------------------------------------------------------------------

    def rank_guesses(current_guesses):
        ranked_guesses = {}
#    invalid = ["!","%","!"]
        tally_dict = {"a":0,
                      "b":0,
                      "c":0,
                      "d":0,
                      "e":0,
                      "f":0,
                      "g":0,
                      "h":0,
                      "i":0,
                      "j":0,
                      "k":0,
                      "l":0,
                      "m":0,
                      "n":0,
                      "o":0,
                      "p":0,
                      "q":0,
                      "r":0,
                      "s":0,
                      "t":0,
                      "u":0,
                      "v":0,
                      "w":0,
                      "x":0,
                      "y":0,
                      "z":0,
                      "\n":0}

        for guess in current_guesses:
            #check = any(item in invalid for item in line)
            #if len(line) != 5: check = True
            #if check == True: pass # if true, word is invalid. if false, add to dictionary. 
            #else:
            word_letters = list()
            for letter in guess:
                if letter not in word_letters: 
                    word_letters.append(letter)
                    tally_dict[letter] += 1
                
    
        tally_dict.pop("\n")
#        print(tally_dict)

        guess_rank_dict = dict()    
        for guess in current_guesses:
            guess_score = 0
            #word_letters = list()
            for letter in guess:
                #if letter not in word_letters:
                    #word_letters.append(letter)
                guess_score += tally_dict[letter]
            guess_rank_dict[guess] = guess_score
        
        ranked_guesses = sorted(guess_rank_dict)

#        for entry in ranked_guesses:
#            print(entry, guess_rank_dict[entry])
            
        print(sorted(guess_rank_dict.items(), key =
             lambda kv:(kv[1], kv[0])))    
        

        return


#-----------------------------------------------------------------------------
#-Back to the main program now

    while guessing == True:
        
        user_guess = list(input("Please enter your guess, cheater: "))
      
        get_correct_letters(user_guess) # returns correct_letters and incorrect_letters
        print(correct_letters, incorrect_letters)
    
        new_guesses = keep_correct(current_guesses,correct_letters)
        current_guesses = new_guesses
        new_guesses = list() 
        print("current guesses", len(current_guesses), "after keep_correct()")
    
        new_guesses = remove_incorrect(current_guesses, incorrect_letters)
        current_guesses = new_guesses
        new_guesses = list()
        print("current guesses", len(current_guesses), "after remove_incorrect")
    
        new_guesses = position_check(current_guesses, user_guess)
        current_guesses = new_guesses
        new_guesses = list()
        print("current guesses ", len(current_guesses), "at end of position_check")
    

        rank_guesses(current_guesses)        

        user_input = input("Still guessing? 'y/n' : ")
        if user_input != 'y': guessing = False

main()
