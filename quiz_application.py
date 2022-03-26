print("Welcome to my computer science quiz")

playing = input("Do you want to attempt the questions? ")


if playing.lower() != "yes":
    quit()

else:
    print("Okay, let's go")

#score of the total marks got

score = 0;

answer = input("What does RAM stand for")
if answer.lower() == "random access memory":
    print("Correct!")
    score+=1;
else:
    print("Incorrect!")


answer = input("What does CPU stand for")
if answer.lower() == "central processing unit":
    print("Correct!")
    score+=1;
else:
    print("Incorrect!")


answer = input("What does GPU stand for")
if answer.lower() == "graphics processing unit":
    print("Correct!")
    score+=1;
else:
    print("Incorrect!")

print("You have scored "+ str(score)+ " questions correct")
print("Your final score is "+ str((score/3)*100)+ "%")




