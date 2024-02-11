import random
import arts

word_list = ["aardvark", "baboon", "camel"]
chosen_word = random.choice(word_list)

#Testing code- this part is for testing purpose only
print(f'Pssst, the solution is {chosen_word}.')
#this is the actual code
display=[]
for i in range(len(chosen_word)):
  display+="_"

lives=6
flag=False
wordFound=False

while(flag==False):
  if(lives>0):
    print(arts.stages[lives])
    guess = input("Guess a letter: ").lower()
    
    for i in range(len(chosen_word)):
      if(chosen_word[i]==guess):
        display[i]=guess
        wordFound=True
    print(display)
    if(wordFound==False):
      lives-=1
      print("\nYou guessed wrong letter and lost a life...\n")
    wordFound=False
      

    if "_" not in display:
      flag=True
      print("\n YOU WIN!\n")
    print()
    print("----------------------------------------------------------\n")
  else:
    flag=True
    print("\n YOU LOSE!")