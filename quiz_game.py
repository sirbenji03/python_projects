print("Welcome to my computer quiz!")

start = input("Do you want to start? ")
print(start)

if start.lower() != "yes":
    quit()

print("Yay! You have started :) ")
score = 0

answer = input("what does cpu stands for? ")
if answer.lower() == "central processing unit":
    print('correct')
    score += 1
else:
    print('incorrect')

answer = input("what does gpu stands for? ")
if answer.lower() == "graphic processing unit":
    print('correct')
    score += 1
else:
    print('incorrect')

answer = input("what does ram stands for? ")
if answer.lower() == "random access memory":
    print('correct')
    score += 1
else:
    print('incorrect')

answer = input("what does psu stands for? ")
if answer.lower() == "power supply unit":
    print('correct')
    score += 1
else:
    print('incorrect')

answer = input("what does rom stands for? ")
if answer.lower() == "read only memory":
    print('correct')
    score += 1
else:
    print('incorrect')

print("you got " + str(score) + " questions correct!")
print("you got " + str((score / 5) * 100) + "%")
