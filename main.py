import random

weights = [213, 300, 200]
locations = [random.randint(1, 8) for _ in range(3)]
print("Hello! Your mission is to guess the locations of 3 buried boxes")

while True:
    guesses = []
    correct_guesses = 0

    for i in range(3):
        while True:
            guess = input(f"Enter your guess for the location of box{i+1} (1-8):")
        
            if guess.isdigit():
                guess = int(guess)
                if 1 <= guess <= 8:
                    guesses.append(guess)
                    break
                else:
                    print("Incorrect. Enter a number between 1 and 8")
    for i in range(3):
        if guesses[i] == locations[i]:
            correct_guesses += 1
    if guesses == locations:
        if sum(weights) == 713:
            print("Congratulations! You found all the boxes")
            print(f"Locations: {locations}, Weights: {weights}")
            break
        else:
            print("Correct locations, but the weights is incorrect. Try again")
    else:
        print(f"Wrong guesses. The boxes are moving to new spots. ") 
        locations = [random.randint(1, 8) for _ in range(3)]
