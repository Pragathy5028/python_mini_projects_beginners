#quiz game
count=0
playing=input("Hello there!!Do you want to join the quiz?:\n")
if playing !="yes":
  quit(print("Maybe next time."))

print("Okey!lets go!!")

Answer=input("What is the full form of gpu?\n")
if Answer.lower()=="graphics processing unit":
  print("Correct!:)")
  count+=1
else:
  print("wrong:(the right answer is graphics processing unit")
Answer=input("What is the full form of cpu?\n")
if Answer.lower()=="central processing unit":
  print("Correct:)")
  count+=1
else:
  print("Wrong:( The correct answer is central processing unit")

print(f"your total score is :\n {count}")
print("you got"+str((count/2)*100)+"%")
