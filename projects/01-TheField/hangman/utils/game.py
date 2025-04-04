import random

class Hangman:

    def __init__ (self):
        
        self.possible_words = ["becode", "learning", "mathematics", "sessions"]
        self.word_to_find = list(random.choice(self.possible_words))
        self.lives = 5
        self.correctly_guessed_letters = ["_" for letter in self.word_to_find]
        self.wrongly_guessed_letters = []
        self.turn_count = 0 
        self.error_count = 0
    
    def play(self):

        while True:
            letter = input ("Write a letter").lower()
            if len(letter) != 1 or not letter.isalpha():
                print ("Please enter only one letter")
            elif letter in self.correctly_guessed_letters or self.wrongly_guessed_letters:
                print ("You've already tried this one")
            else:
                self.turn_count += 1 
                return letter
            
    





