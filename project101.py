import random

response=input("Do you want to roll the dice?")
response == "y"

while response =="y":
  no = random.randint(1,6)
  if no==1:
    print("[---]")
    print("[   ]")
    print("[ 0 ]")
    print("[0 0]")
   
  
  response = input("press y to roll the dice again and n to exit")

