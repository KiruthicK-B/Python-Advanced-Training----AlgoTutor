import json
import os
from datetime import datetime

class InventorySystem:
    def __init__(self, filename='inventory.json'):
        self.filename = filename
        self.inventory = self.load_inventory()
    
    def load_inventory(self):
        
        if os.path.exists(self.filename):
            with open(self.filename, 'r') as f:
                return json.load(f)
        return {}
    
    def save_inventory(self):
        with open(self.filename, 'w') as f:
            json.dump(self.inventory, f, indent=4)
    
    def add_item(self, item_id, name, quantity, price):
        if item_id in self.inventory:
            print(f"Item {item_id} already exists. Use update_quantity instead.")
            return False
        
        self.inventory[item_id] = {
            'name': name,
            'quantity': quantity,
            'price': price,
            'added_date': datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        }
        self.save_inventory()
        print(f"Item '{name}' added successfully!")
        return True
    
    def remove_item(self, item_id):

        if item_id in self.inventory:
            item_name = self.inventory[item_id]['name']
            del self.inventory[item_id]
            self.save_inventory()
            print(f"Item '{item_name}' removed successfully!")
            return True
        print(f"Item {item_id} not found.")
        return False
    
    def update_quantity(self, item_id, quantity_change):
        if item_id in self.inventory:
            self.inventory[item_id]['quantity'] += quantity_change
            self.save_inventory()
            print(f"Quantity updated. New quantity: {self.inventory[item_id]['quantity']}")
            return True
        print(f"Item {item_id} not found.")
        return False
    
    def view_item(self, item_id):
        if item_id in self.inventory:
            item = self.inventory[item_id]
            print(f"\nItem ID: {item_id}")
            print(f"Name: {item['name']}")
            print(f"Quantity: {item['quantity']}")
            print(f"Price: ${item['price']:.2f}")
            print(f"Added: {item['added_date']}")
            return True
        print(f"Item {item_id} not found.")
        return False
    
    def view_all_items(self):
        if not self.inventory:
            print("Inventory is empty.")
            return
        
        print(f"\n{'ID':<10} {'Name':<20} {'Quantity':<10} {'Price':<10} {'Total Value':<15}")
        print("-" * 70)
        
        total_value = 0
        for item_id, item in self.inventory.items():
            item_total = item['quantity'] * item['price']
            total_value += item_total
            print(f"{item_id:<10} {item['name']:<20} {item['quantity']:<10} ${item['price']:<9.2f} ${item_total:<14.2f}")
        
        print("-" * 70)
        print(f"Total Inventory Value: ${total_value:.2f}\n")
    
    def search_items(self, keyword):
        results = {k: v for k, v in self.inventory.items() if keyword.lower() in v['name'].lower()}
        
        if not results:
            print(f"No items found matching '{keyword}'.")
            return
        
        print(f"\nSearch results for '{keyword}':")
        print(f"{'ID':<10} {'Name':<20} {'Quantity':<10} {'Price':<10}")
        print("-" * 50)
        
        for item_id, item in results.items():
            print(f"{item_id:<10} {item['name']:<20} {item['quantity']:<10} ${item['price']:<9.2f}")

def main():
    system = InventorySystem()
    
    while True:
        print("\n=== Inventory Management System ===")
        print("1. Add Item")
        print("2. Remove Item")
        print("3. Update Quantity")
        print("4. View Item")
        print("5. View All Items")
        print("6. Search Items")
        print("7. Exit")
        
        choice = input("\nEnter your choice (1-7): ")
        
        if choice == '1':
            item_id = input("Enter Item ID: ")
            name = input("Enter Item Name: ")
            quantity = int(input("Enter Quantity: "))
            price = float(input("Enter Price: "))
            system.add_item(item_id, name, quantity, price)
        
        elif choice == '2':
            item_id = input("Enter Item ID to remove: ")
            system.remove_item(item_id)
        
        elif choice == '3':
            item_id = input("Enter Item ID: ")
            change = int(input("Enter quantity change (+/-): "))
            system.update_quantity(item_id, change)
        
        elif choice == '4':
            item_id = input("Enter Item ID: ")
            system.view_item(item_id)
        
        elif choice == '5':
            system.view_all_items()
        
        elif choice == '6':
            keyword = input("Enter search keyword: ")
            system.search_items(keyword)
        
        elif choice == '7':
            print("Exiting... Goodbye!")
            break
        
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()