import random
print("Welcome to word guessing game ")
turns = 12
print("You have  ", turns,"chances")
print "THE  THEME IS SPORTS "
words = ['skating', 'kayaking', 'kickboxing', 'badminton',  
            'squash', 'hockey', 'volleyball', 'rugby',  
            'baseball', 'basketball', 'cricket', 'marathon']  
word = random.choice(words) 
print("THIS IS YOUR WORD,") 
guesses = '' 
while turns > 0:
    failed = 0
    for char in word:   
        if char in guesses:  
            print(char)      
        else:  
            print("*") 
            failed += 1
    if failed == 0: 
        print("You Win")  
        print("The word is: ", word)  
        break
    guess = raw_input("NOW,GUESS A CHARACTER IN THESE:") 
    guesses += guess   
    if guess not in word:   
        turns -= 1 
        print("WRONG") 
        print("YOU HAVE", + turns, 'MORE GUESSES') 
        if turns == 0: 
            print("SORRY! YOU LOST,BETTER LUCK NEXT TIME")
    
