from collections import deque

def main():
    # Initialize the lineup using deque
    lineup = deque()
    
    print("Welcome to the Lineup Manager!")
    print("Commands:")
    print("  1. 'add [name]' - Add a person to the lineup.")
    print("  2. 'next' - Serve the next person in the lineup.")
    print("  3. 'remove' - Remove specific person in the lineup")
    print("  4. 'view' - View the current lineup.")
    print("  5. 'exit' - Exit the program.")
    
    while True:
        command = input("\nEnter a command: ").strip().lower()
        
        if command.startswith("add "):
            # Add a person to the lineup
            name = command[4:].strip()
            if name:
                lineup.append(name)
                print(f"{name} has been added to the lineup.")
            else:
                print("Please provide a name after 'add'.")
        
        elif command == "next":
            # Serve the next person in the lineup
            if lineup:
                next_person = lineup.popleft()
                print(f"Serving {next_person}.")
            else:
                print("The lineup is empty.")
        
        elif command.startswith("remove "):
            nama = command[7:].strip()
            if name in lineup:
                lineup.remove(nama)
                print(f"{nama} has been removed from lineup.")
            else:
                print("That name is not found in the lineup.")
        
        elif command == "view":
            # View the current lineup
            if lineup:
                print("Current lineup:", ", ".join(lineup))
            else:
                print("The lineup is empty.")
        
        elif command == "exit":
            print("Goodbye!")
            break
        
        else:
            print("Invalid command. Please try again.")

if __name__ == "__main__":
    main()
