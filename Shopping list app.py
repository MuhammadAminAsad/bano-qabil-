# Shopping List App

# List to store shopping items
shopping_list = []

# Function to display the shopping list
def display_shopping_list():
    if not shopping_list:
        print("Your shopping list is empty.")
    else:
        print("Your shopping list:")
        for item in shopping_list:
            print(f"- {item}")

# Function to add an item to the shopping list
def add_to_shopping_list(item):
    shopping_list.append(item)
    print(f"Added '{item}' to your shopping list.")

# Main function
def main():
    print("Welcome to the Shopping List App!")

    while True:
        print("\nMenu:")
        print("1. Add Item to Shopping List")
        print("2. View Shopping List")
        print("3. Exit")

        choice = input("Enter your choice (1-3): ")

        if choice == "1":
            item = input("Enter the item you want to add: ")
            add_to_shopping_list(item)
        elif choice == "2":
            display_shopping_list()
        elif choice == "3":
            print("Goodbye! Happy shopping! please come again.")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 3.")

# Run the program
if __name__ == "__main__":
    main()