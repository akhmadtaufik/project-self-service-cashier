from cashier import Transaction

user = Transaction()
# Test Case 1
# Add Item 1
print("Test Case 1")
print("-----------")
user.add_item("Ayam Goreng", 15, 20_000)
print("\n")
# Add Item 2
user.add_item("Pasta Gigi", 3, 15_000)
print("\n")
print("Order Table :")
user.check_order()

# Test Case 2
# Delete pasta gigi from order table
print("\n")
print("Test Case 2")
print("-----------")
user.delete_item("Pasta Gigi")
print("Order Table :")
user.check_order()
user.check_out()

# Test Case 3
# Reset all transaction
print("\n")
print("Test Case 3")
print("-----------")
user.reset_transaction()

# Test Case 4
print("\n")
print("Test Case 4")
print("-----------")
# Add Item 1
user.add_item("Ayam Goreng", 2, 20_000)
print("\n")
# Add Item 2
user.add_item("Pasta Gigi", 3, 15_000)
print("\n")
# Add Item 3
user.add_item("Mainan Mobil", 1, 200_000)
print("\n")
# Add Item 4
user.add_item("Mie Instan", 5, 3_000)
print("\n")
print("Order Table :")
user.check_order()
user.check_out()

# Test Case 5
# Update Item, JumlahBarang, dan Harga
print("\n")
print("Test Case 5")
print("-----------")
print("Order Table Before:")
user.check_order()
print("\n")
# Update Item pasta gigi
user.update_item_name("Pasta Gigi", "Sabun Mandi")
# Update JumlahBarang ayam goreng
user.update_item_qty("Ayam Goreng", 3)
# Update Harga mie instan
user.update_item_price("Mie Instan", 3_500)
print("\n")
print("Order Table After:")
user.check_order()

user.check_out()
