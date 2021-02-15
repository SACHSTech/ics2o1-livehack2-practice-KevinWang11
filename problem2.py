mark = int(input("Please enter your average here: "))
earnings = int(input("Please enter your earnings here: "))

if mark >= 80 and earnings >= 500:
  print("You can go to Europe in the summer!")

elif mark >= 80 and earnings < 500:  
  print("You can go to California in the summer!")

else:
  print("You do not get to go anywhere in the summer.")

