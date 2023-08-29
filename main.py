#Title: Minecraft Quiz
#Description: A quiz about Minecraft
#Author: Sean Aitken
#Date created: 2021-09-20

import time
score = 0


print ("Welcome to the Minecraft Quiz!")
time.sleep(1) # Wait for 1 second
print ("You will be asked basic questions about Minecraft.")
time.sleep(1) # Wait for 1 second
print ("If you get a question correct, you will get 10 points.")
time.sleep(1) # Wait for 1 second
print ("If you get a question wrong, you will not get any points.")
time.sleep(1) # Wait for 1 second
print ("Good luck!")
time.sleep(1) # Wait for 1 second
print ("-"*40)


# Ask first question
question = "What is the final boss in minecraft?"
print(question)

# Get the player's answer
player_answer = input("Your answer: ")

# Check if the answer is correct
correct_answer = "ender dragon"
if player_answer.lower() == correct_answer:
    print("Correct!")
    score += 10
elif player_answer.lower() == "enderdragon":
    print("Correct!")
    score += 10
else:
    print("Incorrect!")
    print("Correct answer: Ender Dragon")
    
time.sleep(2) # Wait for 2 seconds


# Ask a question
question = "How many wood planks are needed to make a crafting table?"
print(question)

# Get the player's answer
player_answer = input("Your answer: ")

# Check if the answer is correct
correct_answer = "4"
if player_answer.lower() == correct_answer:
    print("Correct!")
    score += 10
elif player_answer.lower() == "four":
    print("Correct!")
    score += 10
else:
    print("Incorrect!")
    print("Correct answer: 4 wood planks")

time.sleep(2) # Wait for 2 seconds


# Ask a question
question = "What food gives the most hunger points?"
print(question)

# Get the player's answer
player_answer = input("Your answer: ")

# Check if the answer is correct
correct_answer = "steak"
if player_answer.lower() == correct_answer:
    print("Correct!")
    score += 10  
elif player_answer.lower() == "cooked beef":
    print("NO IT IS NOT COOKED BEEF IT IS STEAK!!!")
    print("You lose 5 points")
    score -= 5
else:
    print("Incorrect!")
    print("Correct answer: Steak")
    
time.sleep(2) # Wait for 2 seconds


# Ask a question
question = "What is the hardest inget to get in minecraft?"
print(question)

print("1. Emerald")
print("2. Diamond")
print("3. Gold ingot")
print("4. Netherite ingot")

# Get the player's answer
player_answer = input("Your answer: ")

# Check if the answer is correct
correct_answer = "4"
if player_answer.lower() == correct_answer:
    print("Correct!")
    score += 10
elif player_answer.lower() == "netherite":
    print("Correct!")
    score += 10
elif player_answer.lower() == "netherite ingot":
    print("Correct!")
    score += 10
else:
    print("Incorrect!")
    print("Correct answer: Netherite ingot")

time.sleep(2) # Wait for 2 seconds


# Ask a question
question = "What tool is used to mine ores in minecraft?"
print(question)

print("1. Pickaxe")
print("2. Shovel")
print("3. Axe")
print("4. Hoe")

# Get the player's answer
player_answer = input("Your answer: ")

# Check if the answer is correct
correct_answer = "1"
if player_answer.lower() == correct_answer:
    print("Correct!")
    score += 10
elif player_answer.lower() == "pickaxe":
    print("Correct!")
    score += 10
else:
    print("Incorrect!")
    print("Correct answer: Pickaxe")

time.sleep(2) # Wait for 2 seconds


# Ask a question
question = "What is the best armor in minecraft?"
print(question)

print("1. Diamond armor")
print("2. Netherite armor")
print("3. Iron armor")
print("4. Leather armor")

# Get the player's answer
player_answer = input("Your answer: ")

# Check if the answer is correct
correct_answer = "2"
if player_answer.lower() == correct_answer:
    print("Correct!")
    score += 10
elif player_answer.lower() == "netherite":
    print("Correct!")
    score += 10
elif player_answer.lower() == "netherite armor":
    print("Correct!")
    score += 10
elif player_answer.lower() == "diamond armor":
    print("It used too be diamond armor until netherite was added in 1.16")
else:
    print("Incorrect!")
    print("Correct answer: Netherite armor")
    
time.sleep(2) # Wait for 2 seconds


# Ask a question
question = "How many dimensions are there in minecraft?"
print(question)

# Get the player's answer
player_answer = input("Your answer: ")

# Check if the answer is correct
correct_answer = "3"
if player_answer.lower() == correct_answer:
    print("Correct!")
    score += 10
elif player_answer.lower() == "three":
    print("Correct!")
    score += 10
else:
    print("Incorrect!")
    print("Correct answer: There are 3 dimensions in minecraft")

time.sleep(2) # Wait for 2 seconds


# Ask a question
question = "What mob was accidentally added to minecraft when trying to make a pig?"
print(question)

print("1. Piglin")
print("2. Creeper")
print("3. Pig")
print("4. Zombie pigman")

# Get the player's answer
player_answer = input("Your answer: ")

# Check if the answer is correct
correct_answer = "2"
if player_answer.lower() == correct_answer:
    print("Correct!")
    score += 10
elif player_answer.lower() == "creeper":
    print("Correct!")
    score += 10
else:
    print("Incorrect!")
    print("Correct answer: Creeper Aw man")

time.sleep(1) # Wait for 1 second

# Display the current score
print("Your score: ", score, "/ 80")