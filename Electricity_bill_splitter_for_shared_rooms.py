# Electricity Bill Splitter for Shared Rooms
# Sample data: 3 roommates, 1,800₹ total bill, with different days stayed.

# Sample roommate data
roommates = [
    {"name": "Alice", "days": 30},
    {"name": "Bob", "days": 20},
    {"name": "Charlie", "days": 10}
]

total_bill = 1800  # Total bill in ₹

# Calculate total number of days
total_days = sum([rm['days'] for rm in roommates])

# Print introduction and bill details
print("=== Electricity Bill Splitter for Shared Rooms ===")
print(f"Total Electricity Bill: ₹{total_bill}")
print(f"Total Roommates: {len(roommates)}\n")

# Print roommates data
print("Roommate Details:")
for rm in roommates:
    print(f"  {rm['name']}: {rm['days']} days")

# Split the bill
print("\n--- Bill Split ---")
for rm in roommates:
    share = (rm['days'] / total_days) * total_bill
    print(f"{rm['name']} pays: ₹{share:.2f}")
