import random
user_score = 0
game_score = 0
runprogram = True
while(runprogram):
   user = input("trash compost or recycle: ")
   game = ["trash", "compost", "recylce"]
   ran = random.choice(game)
   print(ran)
   print(f"Your score: {user_score}")
   print(f"Enemies' score: {game_score}")
   if user == ran:
       print("It is a tie")
    elif user == "trash" and game == "recylce":
        print("You lose")
        game_score += 1
    elif user == "trash" and game == "compost":
        print("You win")
        user_score += 1
    elif user == "compost" and game == "trash":
        print("You lose")
        game_score += 1
    elif user == "compost" and game == "recycle":
        print("You win")
        user_score += 1
    elif user == "recycle" and game == "trash":
        print("You win")
        user_score += 1
    elif user == "recycle" and game == "compost":
        print("You lose")
        game_score += 1
    else:
        user = input("trash compost or recycle: ")
    print(f"Your score: {user_score}")
   print(f"Enemies' score: {game_score}")
   again = input("Would you like to play again? ")
   if again == "no":
       runprogram = False 