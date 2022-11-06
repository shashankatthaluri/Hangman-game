import random

#welcoming the users
name1 = raw_input("What is your name? ")
name2 = raw_input("What is your name? ")
print "Hello, " + name1, "Time to play hangman!"
print "Hello, " + name2, "Time to play hangman!"
print "You have a chance to choose the level, Press (1) for easy level.\n(2) for hard level"
#input of the level
user_choice_1 = raw_input("->")

player1_score=0
player2_score=0
#Rules of the game 
print "Rules of the game"
print "Basically you should save yourself out from this trap."
print "What you can do is just follow the rules below."
print "1)The system will give u some blanks which is a word not revealed."
print "2)you should guess that word correctly."
print "3)the number of moves lead you to be get hanged."			
print "are you ready to die?"
print "First,"+ name1, "starts playing,"+ name2, "try to distrub him to win"
#Here starts the game
print "Start guessing..."
#list of word for easy level
wordlist1 = ['hangman','dinner','computer','america','olympics','oscar',
	  'football','minecraft','jacket','cabbage','electricity',
            'pasta','japan','water','programming','anaconda','dog',    
            'name','windows','curtains','wheel','civilization',  
            'bluebird','table','size','guardian','mario','parachute',
            'bioshock','physics','jumping','eating','uranium','obama',
            'youtube','putin','dairy','christianity','coins','heard',
            'mom','executive','car','jade','abrahim','sand','silver',  
            'fizzle','moonman','watermelon','whistle','hesitate','agario', 
             'extreme','wrist','damn','shit','wrong','turtle','church',name1]
#list of words for hard level
wordlist2 = ['wry', 'hymn','cyst', 'myrrh', 'myth', 'wyrm', 'crypt', 
	    'flyby', 'gypsy','lynch', 'nymph', 'pygmy', 'rhythm',
	    'hurdler','purpler','weird','playright','agitating',
	    'kirito','montenegro','clubpenguin','chlorinate',
              'oskahlavistah','dermatoglyphics','misconjugatedly',
              'uncopyrightable','duplicate','abridgment','clustering',
              'angleworms','authorized','algorithms','benchmarks',
              'bifurcated','blacksmith','boundaries','championed',
              'complexity','consumable','crumbliest','deathblows',
              'demography','emulations','exhausting','falterings',
              'forgivable','fulminated','graciously','harlequins',
              'incubator','journalism','labyrinths','lawrencium', name1]
               
#game starts according to user choice               
if   user_choice_1=='1' :               
          
	#here we set the secret
	words = random.randint(0, len(wordlist1))
	word1 = (wordlist1[words])


elif user_choice_1=='2' :
	
	#here we set the secret
	words = random.randint(0, len(wordlist2))
	word1 = (wordlist2[words])

#creates an variable with an empty value
guesses1 = ''

#determine the number of turns
turns1 = 6

# we Create a while loop

#check if the turns are more than zero
while turns1 > 0:         

    # make a counter that starts with zero
    failed1 = 0             

    # for every character in secret_word    
    for char1 in word1:      

    # see if the character is in the players guess
        if char1 in guesses1:    
    
        # print then out the character
            print char1,    

        else:
    
        # if not found, print a blank
            print "_",     
       
        # and increase the failed counter with one
            failed1 += 1    

    # if failed is equal to zero

    # print You guessed correctly
    if failed1 == 0:        
        print "Congrats You guessed correctly, Lets see who is going to be the winner cross your fingers,"+name1   

    # exit the script
        break              

    print

    # ask the user go guess a character
    guess1 = raw_input("guess a character:") 

    # set the players guess to guesses
    guesses1 += guess1                    


	
    # set wrong if player enter anything other than alphabets	
    if guess1.isalpha() == False:
        print "You have to guess a letter, silly!. BTW you lost a chance sorry"	
	
    # set wrong if the input is more then one letter	
    if len(guess1) > 1:
        print "You can't guess more than one letter at a time, silly!. Btw you lost one chance!"	
   
   
    
    	 
    
    # if the guess is not found in the secret word
    if guess1 not in word1:  
 
     # turns counter decreases with 1 (now 5)
        turns1 -= 1       
    
    # prints wrong guess 
        print "Things aren't looking so good, that guess was WRONG!"    
 
    # how many turns are left
        print "You have", + turns1, 'more guesses1' 
 
   
        if turns1 == 5:
    	 print "-------"
    	 print "|      |"
    	 print "|      0"
    	 print "|"
    	 print "|"
    	 print "|"
    	 print "----------" 
         
        if turns1 == 4:
    	 print "-------"
    	 print "|      |"
    	 print "|      0"
    	 print "|      |"
    	 print "|"
    	 print "|"
    	 print "----------"   
            
        if turns1 == 3:
    	 print "-------"
    	 print "|      | "
    	 print "|      0 "
    	 print "|     <|"
    	 print "|"
    	 print "|"
    	 print "----------"    
        if turns1 == 2:
    	 print "-------"
    	 print "|      |"
    	 print "|      0"
    	 print "|     <|>"
    	 print "|"
    	 print "|"
    	 print "----------"
        if turns1 == 1:
    	 print "-------"
    	 print "|      |"
    	 print "|      0"
    	 print "|     <|>"
    	 print "|     / "
    	 print "|"
    	 print "----------"
        if turns1 == 0:
    	 print "-------"
    	 print "|      |"
    	 print "|      0"
    	 print "|     <|>"
    	 print "|     / /"
    	 print "|"
    	 print "----------"

         # if the turns are equal to zero
        if turns1 == 0:           
    
        
            print "Sorry you didn't guess the word correctly,the word is,"+word1, " Lets see if the,"+name2, "guess wrong the game will be tie."



print "its your turn,"+ name2, "try to defeat,"+name1, "with maximum points" 
#Here starts second player  game
print "Start guessing..."
#game starts according to user choice 
if   user_choice_1=='1' :               
              
	#here we set the secret
	words = random.randint(0, len(wordlist1))
	word2 = (wordlist1[words])


elif user_choice_1=='2' :
	
	#here we set the secret
	words = random.randint(0, len(wordlist2))
	word2 = (wordlist2[words])

#creates an variable with an empty value
guesses2 = ''

#determine the number of turns
turns2 = 6

# Create a while loop

#check if the turns are more than zero
while turns2 > 0:         

    # make a counter that starts with zero
    failed2 = 0             

    # for every character in secret_word    
    for char2 in word2:      

    # see if the character is in the players guess
        if char2 in guesses2:    
    
        # print then out the character
            print char2,    

        else:
    
        # if not found, print a blank
            print "_",     
       
        # and increase the failed counter with one
            failed2 += 1    

    # if failed is equal to zero

    
    if failed2 == 0:        
        print "Congrats You guessed correctly Lets see who is going to be the winner cross your fingers,"+name2  

    # exit the script
        break              

    print

    # ask the user go guess a character
    guess2 = raw_input("guess a character:") 

    # set the players guess to guesses
    guesses2 += guess2                    
     
      # set wrong if player enter anything other than alphabets
    if guess2.isalpha() == False:
        print "You have to guess a letter, silly!. BTW you lost a chance sorry"	

    # set wrong if the input is more then one letter
    if len(guess2) > 1:
        print "You can't guess more than one letter at a time, silly!. BTW you lost a chance sorry!"


    # if the guess is not found in the secret word
    if guess2 not in word2:  
 
     # turns counter decreases with 1 (now 5)
        turns2 -= 1        
 
    # print wrong
        print "Things aren't looking so good, that guess was WRONG!"    
 
    # how many turns are left
        print "You have", + turns2, 'more guesses2' 
 
     # picturization of the game  
        if turns2 == 5:
    	 print "-------"
    	 print "|      |"
    	 print "|      0"
    	 print "|"
    	 print "|"
    	 print "|"
    	 print "----------" 
         
        if turns2 == 4:
    	 print "-------"
    	 print "|      |"
    	 print "|      0"
    	 print "|      |"
    	 print "|"
    	 print "|"
    	 print "----------"   
            
        if turns2 == 3:
    	 print "-------"
    	 print "|      | "
    	 print "|      0 "
    	 print "|     <| "
    	 print "|"
    	 print "|"
    	 print "----------"    
        if turns2 == 2:
    	 print "-------"
    	 print "|      |"
    	 print "|      0"
    	 print "|     <|>"
    	 print "|"
    	 print "|"
    	 print "----------"
        if turns1 == 1:
    	 print "-------"
    	 print "|      |"
    	 print "|      0"
    	 print "|     <|>"
    	 print "|     / "
    	 print "|"
    	 print "----------"
        if turns2 == 0:
    	 print "-------"
    	 print "|      |"
    	 print "|      0"
    	 print "|     <|>"
    	 print "|     / /"
    	 print "|"
    	 print "----------"
    	 
    	 
        # if the turns are equal to zero
        if turns2 == 0:           
    	
    	
    	 print "Sorry you didn't guess the word correctly,the word is,"+word2
#players score according to their mistakes         
player1_score=player1_score + turns2
print player1_score,player2_score
player2_score=player2_score + turns1
if player1_score > player2_score:
	print "Congratulations Mr."+name2, "you won the game"
elif player1_score < player2_score:
	print "Congratulations Mr."+name1, "you won the game"
else :
	print "The game is tie. Play again."        



          
            

       
        
        
        	
            
