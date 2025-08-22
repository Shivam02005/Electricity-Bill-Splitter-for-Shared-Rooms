# Electricity Bill Splitter for Shared Rooms

A tiny Python script to fairly divide a shared room’s electricity bill among roommates based on the number of days each person stayed.

## Features
- Pro‐rata splitting using *days stayed* as weight  
- No external dependencies - just Python’s built-ins  
- Fully self-contained; paste and run

## How It Works
1. List each roommate with the number of days they stayed in the billing period.  
2. Provide the total electricity bill amount (in ₹).  
3. The script totals the days, computes each roommate’s share, and prints a neat breakdown.

```
share = (days_stayed / total_days) * total_bill
```

## Usage

1. Make sure Python 3.x is installed.  
2. Save the script as `bill_splitter.py`.  
3. Modify the `roommates` list and `total_bill` variable to match your data.  
4. Run:

```bash
python bill_splitter.py
```

### Example

Input (in the script):

```python
roommates = [
    {"name": "Alice", "days": 30},
    {"name": "Bob", "days": 20},
    {"name": "Charlie", "days": 10}
]

total_bill = 1800  # in ₹
```

Output:

```
=== Electricity Bill Splitter for Shared Rooms ===
Total Electricity Bill: ₹1800
Total Roommates: 3

Roommate Details:
  Alice: 30 days
  Bob: 20 days
  Charlie: 10 days

--- Bill Split ---
Alice pays: ₹900.00
Bob pays: ₹600.00
Charlie pays: ₹300.00
```

## Customizing
- Add or remove roommates by editing the `roommates` list.  
- Use any currency symbol; just change the literal in the print statements.  
- Want to factor in fixed service charges? Add them equally before or after the proportional split.
