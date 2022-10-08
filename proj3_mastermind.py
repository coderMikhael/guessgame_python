import random
name=input("Enter your name: ")
print("Good Luck ", name, "Start Guessing...")
def play():
    word=str(random.randrange(1000,9999))
    flag=0
    guess=''
    turns=0
    while(flag==0):
      failed=0
      for ch in word:
        if ch in guess:
            print(ch, end=' ')
        else:
            print("_")
            print(end=' ')
            failed+=1
      if failed==0:
         print("You Win!!!")
         print("The number: ",  word)
         flag=1
         break;
      gu=input("Guess number: ")
      guess+=gu
      if gu not in word:
         print("Wrong Guess.")
         turns+=1
    return turns
print("Chance for Player1: ")
p1=play()
print("Chance for Player2: ")
p2=play()
if(p1>p2):
    print("Player 2 is Mastermind.")
elif(p1<p2):
    print("Player 1 is Mastermind.")
else:
    print("Both are Mastermind.")        

