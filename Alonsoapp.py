#Directions: Create a Rock, Paper, Scissors game that allows the user to play against the computer. The program should prompt the user to enter their choice, then randomly select a choice for the computer. The program should then determine the winner and print the result. The program should continue to play until the user chooses to exit.
#The program should have the following functions:
#Requiements: Save the functions in a separate file called groupex.py and import them into the main program.

#Function to get user input
def get_user_input():
    userInput = input("Please enter your choice (Rock, Paper, Scissors, Exit): ")

    if userInput in ("Rock", "Paper", "Scissors", "Exit"):
        return userInput
    else:
        return "Invalid choice. Please enter Rock, Paper, Scissors, or Exit"
#Request User Input
#Validate User Input using IN operator and LIST
#Return User Input

#Function to get computer's choice
def get_computer_choice():
    import random 
    choices = ["Rock", "Paper", "Scissors", "Exit"]
    return random.choice(choices)

#Create a list of choices
#Return a random choice from the list
#To use random choices, import random module, and use random.choice() method

#Function to determine the winner
#Compare user's choice and computer's choice
def get_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "Its a tie!"
    elif user_choice == "Rock" and computer_choice == "Scissors":
        return "You win!"
    elif user_choice == "Paper" and computer_choice == "Rock":
        return "You win!"
    elif user_choice == "Scissors" and computer_choice == "Paper":
        return "You win!"
    else:
        return "Computer wins!"
    
#IF both choices are the same
    #Return "It's a tie!"
#ELSE IF user's choice is rock and computer's choice is scissors
    #Return "You win!"
#ELSE IF user's choice is paper and computer's choice is rock
    #Return "You win!"
#ELSE IF user's choice is scissors and computer's choice is paper
    #Return "You win!"
#ELSE IF user's choice is exit
    #Return "exit"
#ELSE
    #Return "Computer wins!"


#START main
#PRINT welcome message
gameOn = True

while gameOn: 
    print("Welcome to my Rock, Paper Scissors game! Please enter your choice.")
    #CALL a function to get user input and store the result as a variable (user_choice)
    user_choice = get_user_input()
    print("You chose: ", user_choice)

    if user_choice == "Exit":
        gameOn = False
        print("Thanks for playing!")
        break
    #CALL a function to get computer's choice and store the result as variable (computer_choice)
    computer_choice = get_computer_choice()
    print("Computer chose: ", computer_choice)
    #PRINT both user and computer choices
    #CALL a function to decide the winner between two choises (user_choice and computer_choice)
    result = get_winner(user_choice, computer_choice)
    #PRINT the result of the game
    print(result)
    #LOOP until the game is over with the user's choice


#END main