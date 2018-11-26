import random

num_of_iterations = int(input("Number of iterations: "))

wins_when_switching = 0
wins_when_not_switching = 0

for i in range(num_of_iterations):
    true_door = random.randint(1, 3)
    print(f"Prize is behind door {true_door}")

    contestant_choice = random.randint(1, 3)
    print(f"Contestant chooses door {contestant_choice}")
    
    host_opens = 1
    while host_opens == true_door or host_opens == contestant_choice:
        host_opens += 1

    print(f"Host opens door {host_opens}")

    contestant_switches = random.randint(0, 1)
    
    final_choice = contestant_choice
    if contestant_switches:
        final_choice = 6 - (host_opens + contestant_choice)
        print(f"Contestant switches from door {contestant_choice} to door {final_choice}")
    else:
        print("Contestant doesn't switch the door")

    if final_choice == true_door:
        print("Contestant won!")
        if contestant_switches:
            wins_when_switching += 1
        else:
            wins_when_not_switching += 1
    else:
        print("Contestant Lost!")
        if contestant_switches:
            wins_when_not_switching += 1
        else:
            wins_when_switching += 1
    print()
    
prob_when_switching = wins_when_switching / num_of_iterations
prob_when_not_switching = wins_when_not_switching / num_of_iterations

print(f"Probability of winning when switching: {prob_when_switching:4.2f}")
print(f"Probability of winning when NOT switching: {prob_when_not_switching:4.2f}")
