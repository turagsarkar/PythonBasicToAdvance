print("Welcome to quiz game!")

playing = input("Do you want to play? ")

if playing.lower() != "yes":
    quit()

print("Okay! Let's play :)")
score = 0

answer = input("What does CPU stand for? ")
if answer.lower() == "central processing unit":
    print('Correct!')
    score += 10
else:
    print("Incorrect!")
    score-=5

answer = input("What does GPU stand for? ")
if answer.lower() == "graphics processing unit":
    print('Correct!')
    score += 10
else:
    print("Incorrect!")
    score-=5

answer = input("What does RAM stand for? ")
if answer.lower() == "random access memory":
    print('Correct!')
    score += 10
else:
    print("Incorrect!")
    score-=5

answer = input("What does PSU stand for? ")
if answer.lower() == "power supply":
    print('Correct!')
    score += 10
else:
    print("Incorrect!")
    score-=5

print("You got " + str(score) + " point!")
print("You got " + str((score / 4) * 100) + "%.")