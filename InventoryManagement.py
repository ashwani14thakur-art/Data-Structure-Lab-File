##  Inventory Management

MAX_CAPACITY = 100 

inventory = []

def insert_product():
    if len(inventory) >= MAX_CAPACITY:
        print("Error: Inventory capacity reached, cannot add more products.")
        return

    sku = input("Enter SKU: ").strip()
    if not sku:
        print("SKU cannot be empty.")
        return

    # Check if SKU exists
    for item in inventory:
        if item['sku'] == sku:
           
            print(f"Product with SKU {sku} already exists.")
            choice = input("Do you want to update the quantity? (y/n): ").lower()
            if choice == 'y':
                try:
                    new_qty = int(input("Enter new quantity: "))
                    if new_qty < 0:
                        print("Error: Quantity must be positive.")
                        return
                except ValueError:
                    print("Invalid input. Quantity must be a number.")
                    return
                item['quantity'] = new_qty
                print(f"Product SKU {sku} quantity updated to {new_qty}.")
            else:
                print("No changes made.")
            return

    name = input("Enter Product Name: ").strip()
    if not name:
        print("Error: Product name cannot be empty.")
        return

    try:
        quantity = int(input("Enter Quantity: "))
        if quantity < 0:
            print("Error: Quantity must be positive.")
            return
    except ValueError:
        print("Invalid input. Quantity must be a number.")
        return

    product = {'sku': sku, 'name': name, 'quantity': quantity}
    inventory.append(product)
    print("Product inserted successfully.")

def insert_multiple_products():
    while True:
        if len(inventory) >= MAX_CAPACITY:
            print("Error: Inventory capacity reached, cannot add more products.")
            break

        insert_product()

        cont = input("Do you want to insert another product? (y/n): ").lower()
        if cont != 'y':
            break

def display_inventory():
    if not inventory:
        print("Inventory is empty.")
        return
    print("\nCurrent Inventory:")
    print(f"{'SKU':<15}{'Product Name':<25}{'Quantity':<10}")
    print("-" * 55)
    for item in inventory:
        print(f"{item['sku']:<15}{item['name']:<25}{item['quantity']:<10}")
    print()

def search_by_sku():
    sku = input("Enter SKU to search: ").strip()
    for item in inventory:
        if item['sku'] == sku:
            print(f"Product found:\nSKU: {item['sku']}\nName: {item['name']}\nQuantity: {item['quantity']}")
            return
    print("Product not found.")

def search_by_name():
    name = input("Enter Product Name to search: ").strip().lower()
    found = False
    for item in inventory:
        if item['name'].lower() == name:
            print(f"Product found:\nSKU: {item['sku']}\nName: {item['name']}\nQuantity: {item['quantity']}")
            found = True
    if not found:
        print("Product not found.")

def delete_product():
    sku = input("Enter SKU to delete: ").strip()
    for i, item in enumerate(inventory):
        if item['sku'] == sku:
            removed_product = inventory.pop(i)
            print(f"Product {removed_product['name']} with SKU {sku} removed from inventory.")
            return
    print("Product not found.")

def main():
    while True:
        print("\nInventory Stock Manager")
        print("1. Insert New Product(s)")
        print("2. Display Inventory")
        print("3. Search Product by SKU")
        print("4. Search Product by Name")
        print("5. Delete Product by SKU")
        print("6. Exit")
        choice = input("Enter your choice (1-6): ")

        if choice == '1':
            insert_multiple_products()  
        elif choice == '2':
            display_inventory()
        elif choice == '3':
            search_by_sku()
        elif choice == '4':
            search_by_name()
        elif choice == '5':
            delete_product()
        elif choice == '6':
            print("Exiting Inventory Manager.")
            break
        else:
            print("Invalid choice. Please select from 1 tDo 6.")

if __name__ == "__main__":
    main()
