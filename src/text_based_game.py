

# Sutton Behie
"""Project Two: Text-Based Adventure Game."""

def show_instructions():
    """Display the game objective and available commands."""
    print("Welcome to: Clean the mess to make the Cake Game!")
    print("Collect the 6 supplies to clean the kitchen mess and make your moms birthday cake.")
    print("To move between rooms type: go north, go east, go west, go south.")
    print("To get items, type: get 'whatever item is in that room'.")
    print("Good luck on cleaning the kitchen!")

def show_status(current_room, inventory, rooms):
    """Display the player's current game status."""
    # lets player know where they are currently standing and what is in their bag
    print(f"\nYou are in the {current_room}")
    print(f"Inventory: {inventory}")

def main():
    # dictionary links rooms to its correct directions and items
    rooms = {
        'Living room': {
            'East': 'Towel closet'
        },
        'Towel closet': {
            'West': 'Living room',
            'East': 'Bathroom',
            'item': 'Kitchen towels'
        },
        'Bathroom': {
            'West': 'Towel closet',
            'East': 'Cleaning closet',
            'South': 'Bedroom',
            'item': 'Mop'
        },
        'Cleaning closet': {
            'West': 'Bathroom',
            'item': 'Cleaning spray'
        },
        'Bedroom': {
            'North': 'Bathroom',
            'South': 'Laundry room',
            'item': 'Broom'
        },
        'Laundry room': {
            'North': 'Bedroom',
            'South': 'Pantry closet',
            'item': 'Scrub daddy'
        },
        'Pantry closet': {
            'North': 'Laundry room',
            'West': 'Kitchen',
            'item': 'Flour'
        },
        'Kitchen': {
            'East': 'Pantry closet'
            # villain room — no item game should finish if player has items 
        }
    }

    # player starts in the Living room with an empty bag and set our win goal
    current_room = 'Living room'
    inventory = []
    winning_item_count = 6

    # print rules and instructions first thing
    show_instructions()

    # keeps the game running in a continuous loop until the player wins, loses, or quits
    while True:
        # shows the player their current location and items before taking their input
        show_status(current_room, inventory, rooms)
        
        # check if there's an item in the room and display it if we haven't picked it up yet
        if "item" in rooms[current_room] and rooms[current_room]["item"] not in inventory:
            print(f"You see a {rooms[current_room]['item']}")
        print("-" * 50)

        # get the player's typed command and split it into words
        move = input("Enter your move: ").strip()
        move_parts = move.split()

        # if they hit enter without typing anything, catch it and ask again
        if len(move_parts) == 0:
            print("Wrong command. Please enter a correct move or item command.")
            continue

        # grab the command (like 'go' or 'get') in lowercase
        command = move_parts[0].lower()

        
        if command == 'go':
            if len(move_parts) > 1:
                direction = move_parts[1].capitalize()
                # check if the requested direction is te correct path from the current room
                if direction in rooms[current_room]:
                    current_room = rooms[current_room][direction]
                    
                    # ff the player stumbles into the Kitchen (villain room) too early, player loses game
                    if current_room == 'Kitchen':
                        if len(inventory) < winning_item_count:
                            show_status(current_room, inventory, rooms)
                            print("uh oh...GAME OVER!")
                            print("Thanks for playing!.")
                            break
                else:
                    print("You can't go that way!")
            else:
                print("Specify a direction (e.g., go East).")

        # how to pick up items in the room
        elif command == 'get':
            if len(move_parts) > 1:
                item_name = " ".join(word.capitalize() for word in move_parts[1:])
              
                if item_name.lower() == 'kitchen towels':
                    item_name = 'Kitchen towels'
                elif item_name.lower() == 'scrub daddy':
                    item_name = 'Scrub daddy'
                elif item_name.lower() == 'cleaning spray':
                    item_name = 'Cleaning spray'
                
                # checks if the item is actually in this room
                if "item" in rooms[current_room] and rooms[current_room]["item"] == item_name:
                    if item_name not in inventory:
                        inventory.append(item_name)
                        print(f"You picked up the {item_name}!")
                        
                        # check to see if the player has collected all 6 items to win the game
                        if len(inventory) == winning_item_count:
                            print("\nYay! You have collected all items and cleaned the kitchen in time to make you moms cake!")
                            print("Thanks for playing!")
                            break
                    else:
                        print("You already have this item.")
                else:
                    print(f"Can't find {item_name} in this room.")
            else:
                print("Specify an item to get (e.g., get Mop).")

        # Allow the user to quit out of the game safely
        elif command == 'quit' or command == 'exit':
            print("Thanks for playing!")
            break
        else:
            print("Wrong command. Use 'go [direction]' or 'get [item name]'.")

if __name__ == '__main__':
    main()


