# Hangman-Game
answer_word = str("TEST")
hidden_word = ["_"]*len(answer_word)
remaining_mistakes = 6

hangman={0:'''
        ____________
         |



         ''',
        1:'''
        ____________
         |
         O


         ''',
        2:'''
        ____________
         |
         O
        /

        ''',
        3:'''
        ____________
         |
         O
        / \\

        ''',
        4:'''
        ____________
         |
         O
        / \\
         |
         ''',
        5:'''
        ____________
         |
         O
        / \\
         |
        /''',
        6:'''
        ____________
         |
         O
        / \\
         |
        / \\ '''}
#The actual Game
while remaining_mistakes > 0:
  #print the hidden word
  print(f"Hidden word is {hidden_word}")
  #print stick figure
  print(hangman[6-remaining_mistakes])
  #ask user for letter
  picked_letter = input("Enter your letter!").upper()
  if picked_letter in answer_word:
    index_count = 0
    # Check if Picked Letter is in the Answer word:               
    for letter in answer_word:
        if letter == picked_letter:
            hidden_word[index_count] = picked_letter
        index_count += 1
    print(f"Correct! {hidden_word}")    
    if hidden_word.count("_") <= 0:
        print ("Congrats!")
        break
  else:
    remaining_mistakes -=1
    print(f"Nope, you have {remaining_mistakes} mistakes left!")
    if remaining_mistakes == 0:
       print("Game over!")