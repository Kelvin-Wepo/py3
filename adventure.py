def choose_three(option1, option2, option3):
    while True:
        response = input(f"Choose an option:\n{option1}\n{option2}\n{option3}\n")
        response = response.upper()
        if response == "A" or response == "B" or response == "C":
            return response
        else:
            print("Invalid response. Please choose A, B, or C.")


def adventure():
    print("You are stranded on a deserted island. What do you do?")
    decision1 = choose_three("A. Build a shelter", "B. Look for food", "C. Try to make a fire")
    
    if decision1 == "A":
        print("You build a shelter and settle in for the night. The next morning, you wake up feeling refreshed and ready to continue your survival journey.")
        decision2 = choose_three("A. Explore the island", "B. Gather resources", "C. Go fishing")
        
        if decision2 == "A":
            print("As you explore the island, you stumble upon a hidden cave. Inside, you find a treasure chest filled with valuable gems and coins. Congratulations, you found the treasure and survived!")
            return True
        
        elif decision2 == "B":
            print("As you gather resources, you accidentally step on a poisonous plant and become ill. Without access to medicine, you perish.")
            return False
        
        else: # decision2 == "C"
            print("You catch a few fish and cook them over an open flame. Unfortunately, the smoke attracts a group of hungry predators who overpower you. Game over.")
            return False
    
    elif decision1 == "B":
        print("You search the island for food, but come across a venomous snake. What do you do?")
        decision3 = choose_three("A. Try to kill the snake", "B. Run away", "C. Stay still and hope it goes away")
        
        if decision3 == "A":
            print("You try to kill the snake, but it bites you first. You die from the venom.")
            return False
        
        elif decision3 == "B":
            print("You run away from the snake and accidentally step into a quicksand trap. Unable to escape, you suffocate and perish.")
            return False
        
        else: # decision3 == "C"
            print("You stay still and the snake eventually slithers away. You continue searching for food and come across a fruit tree. You eat the fruit and survive!")
            return True
    
    else: # decision1 == "C"
        print("You try to make a fire, but the wind keeps extinguishing it. What do you do?")
        decision4 = choose_three("A. Keep trying to make a fire", "B. Find a cave to shelter in", "C. Climb a tree to look for a passing ship")
        
        if decision4 == "A":
            print("You eventually succeed in making a fire, but it quickly gets out of control and burns down the entire forest. You perish in the flames.")
            return False
        
        elif decision4 == "B":
            print("You find a cave and shelter in it, but a flash flood occurs and you drown.")
            return False
        
        else: # decision4 == "C"
            print("As you climb the tree, you spot a passing ship in the distance. You light a signal fire and the ship rescues you. Congratulations, you've been saved!")
            return True
