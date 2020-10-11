import random
runprogram = True
while(runprogram):
   user = input("Trash Compost or Recycle: ")
   game = ["trash", "compost", "recylce"]
   ran = random.choice(game)
   print(ran)