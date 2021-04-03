#Write your code below this line 👇
#Hint: Remember to import the random module first. 🎲

import random
print("welcome to the coin toss")
pick = input('choose heads or tails, ready to flip coin Type "flip"')
toss = random.randint(0,1)
if pick == "flip":
  if toss == 1:
    print("the coin fliped and landed on heads")
  else:
    print("the coin landed on tails")