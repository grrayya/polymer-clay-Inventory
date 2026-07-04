import json
import os
from rich.console import Console
from rich.table import Table

FILE_NAME = "inventory.json"
console = Console()

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
    """Renders the current inventory as a formatted table."""
    table = Table(title="🌸 Aesthetic Stress Relief Inventory 🌸", style="magenta")
    
    table.add_column("Item Name", style="cyan", justify="left")
    table.add_column("Quantity in Stock", style="green", justify="right")
    
    for item, quantity in inventory.items():
        qty_str = str(quantity)
        if quantity <= 5:
            qty_str = f"[red]{quantity}[/red]"
            
        table.add_row(item, qty_str)
        
    console.print(table)
    print("\n")

# --- Input Validation Helpers ---
def get_valid_string(prompt):
    """Ensures the user doesn't enter an empty or whitespace-only string."""
    while True:
        value = input(prompt).strip()
        if value:
            return value
        print("⚠️ Input cannot be empty. Please try again.")

def get_valid_int(prompt):
    """Catches ValueErrors if the user types letters instead of numbers."""
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("⚠️ Invalid input. Please enter a whole number.")

def main():
    inventory = load_inventory()
    
    while True:
        display_stock(inventory)
        print("1. Add or Subtract from existing stock")
        print("2. Set exact stock level (or Create new item)")
        print("3. Remove an item entirely")
        print("4. Exit")
        
        choice = input("Select an option: ").strip()
        
        if choice == '1':
            item = get_valid_string("Enter item name: ")
            
            if item not in inventory:
                print(f"⚠️ '{item}' doesn't exist in inventory. Use Option 2 to create it.")
                continue
                
            qty = get_valid_int("Enter amount to add/remove (e.g., 5 or -3): ")
            new_total = inventory[item] + qty
            
            # Guard against negative inventory
            if new_total < 0:
                print(f"⚠️ Cannot reduce stock below 0. Current stock is {inventory[item]}.")
            else:
                inventory[item] = new_total
                save_inventory(inventory)
                print(f"✅ Updated {item}! New total: {inventory[item]}")
                
        elif choice == '2':
            item = get_valid_string("Enter item name: ")
            qty = get_valid_int("Enter exact stock amount: ")
            
            # Guard against setting negative inventory
            if qty < 0:
                print("⚠️ Stock cannot be set to a negative number.")
            else:
                inventory[item] = qty
                save_inventory(inventory)
                print(f"✅ Set {item} to {qty}!")
                
        elif choice == '3':
            item = get_valid_string("Enter the exact name of the item to delete: ")
            if inventory.pop(item, None) is not None:
                save_inventory(inventory)
                print(f"🗑️ Deleted {item} from inventory.")
            else:
                print(f"⚠️ Could not find '{item}'. Check your spelling.")
                
        elif choice == '4':
            print("Exiting tracker...")
            break
            
        else:
            print("⚠️ Invalid choice. Please enter 1, 2, 3, or 4.")

if __name__ == "__main__":
    main()
