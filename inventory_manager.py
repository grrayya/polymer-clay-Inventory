import json
import os

FILE_NAME = "inventory.json"

def load_inventory():
    """Reads the JSON file or creates a default one if it doesn't exist."""
    if not os.path.exists(FILE_NAME):
        default_stock = {
            "Glazed Penguin Charms": 15,
            "Mini Food Keycaps": 30,
            "Earrings": 20
        }
        save_inventory(default_stock)
        return default_stock
    
    with open(FILE_NAME, "r") as file:
        return json.load(file)

def save_inventory(data):
    """Writes the dictionary back to the JSON file."""
    with open(FILE_NAME, "w") as file:
        json.dump(data, file, indent=4)

def display_stock(inventory):
    print("\n--- Current Inventory ---")
    for item, quantity in inventory.items():
        print(f"📦 {item}: {quantity} in stock")
    print("-------------------------\n")

def main():
    inventory = load_inventory()
    
    while True:
        display_stock(inventory)
        print("1. Update stock (Add/Subtract/Create)")
        print("2. Remove an item entirely")
        print("3. Exit")
        
        choice = input("Select an option: ")
        
        if choice == '1':
            item = input("Enter item name (e.g., Glazed Penguin Charms): ")
            qty = int(input("Enter amount to add/remove: "))
            
            if item in inventory:
                inventory[item] += qty
            else:
                inventory[item] = qty
                
            save_inventory(inventory)
            print(f"✅ Updated {item}!")
            
        elif choice == '2':
            item = input("Enter the exact name of the item to delete: ")
            # Using .pop() safely removes the key if it exists
            if inventory.pop(item, None) is not None:
                save_inventory(inventory)
                print(f"🗑️ Deleted {item} from inventory.")
            else:
                print(f"⚠️ Could not find '{item}'. Check your spelling.")
                
        elif choice == '3':
            print("Exiting tracker...")
            break

if __name__ == "__main__":
    main()
