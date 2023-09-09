import random as r

def roll():
  min_value=1
  max_value=6
  value=r.randint(min_value,max_value)

  return value

# v=roll()
# print(v)
while True:
  players=input("Enter the Number of players between 2 to 4: ")
  if(players.isdigit()):
    players=int(players)
    if(2<=players<=4):
      break
    else:
      print("Enter the number between 2 to 4")
  else:
    print("Invalid,Try again")

max_score=20
players_score=[0 for i in range(players)]

print(players_score)

while max(players_score)<max_score:
  for players_id in range(players):
    print("\nPlayer ",players_id+1,"has started")
    print()
    print("Your total score is",players_score[players_id],"\n")
    current_score=0

    while True:
      should_roll=input("Do you want to roll the dice (y/n): ")
      if(should_roll.lower()=="y"):
        value=roll()
      else:
        break


      if(value==1):
        # current_score=0
        print("You rolled a 1,Turn doned !")
        break
      else:
        current_score+=value
        print("You rolled a ",value)


      print("Your score is ",current_score)
    players_score[players_id]+=current_score
    print("The",players_id+1,"total score is: ",players_score[players_id])
max_score=max(players_score)
winner_id=players_score.index(max_score)

print("Player Number",winner_id+1,"is the Winner with Score",max_score)



