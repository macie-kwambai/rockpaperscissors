#Import required modues
import sys
import getpass
import random
import time


#Find winner and add points
def compare(human_ans, comp_ans, human_points, computer_points):
    if human_ans is comp_ans:
        return("It's a tie!")

    elif human_ans is 1 and comp_ans is 2:
        computer_points += 1
        return ("%s (Paper) beats %s (Rock)" %(str(computer), str(human)))

    elif human_ans is 1 and comp_ans is 3:
        human_points += 1
        return ("%s (Rock) beats %s (Scissors)" %(str(human), str(computer)))

    elif human_ans is 2 and comp_ans is 1:
        human_points += 1
        return ("%s (Paper) beats %s  (Rock)" %(str(human), str(computer)))

    elif human_ans is 2 and comp_ans is 3:
        computer_points += 1
        return ("%s (Scissors) beats %s  (Paper)" %(str(computer), str(human)))

    elif human_ans is 3 and comp_ans is 1:
        human_points += 1
        return ("%s (Rock) beats %s (Scissors)" %(str(human), str(computer)))

    elif human_ans is 3 and comp_ans is 2:
        human_points += 1
        return ("%s (Scissors) beats %s  (Paper)" %(str(human), str(computer)))
    else:
        return ("Wrong input!")


def play():
    computer_answer = random.randint(1,3) #Computer makes move
    time.sleep(1) #Sleep to simulate the human time taken to come up with a move
    choices = "Your turn...\n\t[1] Rock\n\t[2] Paper \n\t[3] Scissors\n"
    human_answer = input(choices)
    print ("My move was " + str(computer_answer))
    print(compare (int(human_answer), int(computer_answer), int(human_points), int(computer_points)))
    return 0




#################### Start program ###################
if __name__ == "__main__":
    #Get computer name, player's name and number of game passes    
    human_points = 0    
    computer_points = 0
    computer = getpass.getuser()
    human = input("Hello there human. My name is " + computer + ". \nWhat's yours? \n")
    moves = input ("Alrighty " + human + ". Let's see if the brain really is smarter than the processor :P\n\nFirst enter the number moves we'll play before tallying the results:\n" )
    for i in range (int(moves)):
        play()
    if human_points > computer_points:
        print("%s wins with %i points against %s's %i points. " %(str(human), int(human_points), str(computer), int(computer_points)))
    else:
        print("%s wins with %i points against %s's %i points. " %(str(computer), int(computer_points,), str(human), int(human_points)))

    sys.exit() #Exit
