'''This is task 1.1 of MIA Summer training for AI SUB-TEAM
Program created and programmed by: Yassin Khaled, CCE28
Required to do :
##1. Create a program that displays the gear based on the gear number. Done
##2. Initialize a 5x4 grid to represent the gear display. Done
##3. Loop for user input to enter the gear number. Done
##4. Neutral gear is represented by 0. Done
##5. Exited when the user enters -1. Done
'''


def display_gear(gear_number):
    """Display the gear based on the gear number."""
    gear_list = [[' ' for _ in range(4)] for _ in range(5)]  # Init 5x4 grid
    patterns = {
        0: [  # Zero
            "####",
            "#  #",
            "#  #",
            "#  #",
            "####"
        ],
        1: [  # One
            "   #",
            "   #",
            "   #",
            "   #",
            "   #"
        ],
        2: [  # Two
            "####",
            "   #",
            "####",
            "#   ",
            "####"
        ],
        3: [  # Three
            "####",
            "   #",
            "####",
            "   #",
            "####"
        ],
        4: [  # Four
            "#  #",
            "#  #",
            "####",
            "   #",
            "   #"
        ],
        5: [  # Five
            "####",
            "#   ",
            "####",
            "   #",
            "####"
        ],
        6: [  # Six
            "####",
            "#   ",
            "####",
            "#  #",
            "####"
        ],
        7: [  # Seven
            "####",
            "   #",
            "   #",
            "   #",
            "   #"
        ],
        8: [  # Eight
            "####",
            "#  #",
            "####",
            "#  #",
            "####"
        ]
    }

    # Check if the gear number is valid
    if 0 <= gear_number <= 8:
        if gear_number == 0:
            print('Neutral Gear')
        else:
            print(f'Gear {gear_number}')
        for i in range(5):
            gear_list[i] = list(patterns[gear_number][i])
    else:
        print("Invalid gear number. Please enter a number between 0-8.")
    for row in gear_list:
        print(''.join(row))
        
  
# Main loop to get user input and display the gear      
while True:
    try:
        user_input = input("Enter the gear number (0-8, or -1 to exit): ")
        gear_number = int(user_input)
        if gear_number == -1: #to be able to exit the program
            print("Exiting the program............")
            break
        elif 0 <= gear_number <= 8:
            display_gear(gear_number)
            print("Gear display complete.")
        else:
            print("Invalid gear number. Please enter a number between 0-8.")
    except ValueError:
        print('Please enter a valid number.')
# End of Task 1.1