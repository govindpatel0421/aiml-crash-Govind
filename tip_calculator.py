def calculate_tip(bill, tip_percent):
    tip_amount = bill * (tip_percent / 100)
    total_amount = bill + tip_amount

    return {
        "tip": tip_amount,
        "total": total_amount
    }

# Test cases
bill1 = calculate_tip(500, 10)
bill2 = calculate_tip(1200, 15)
bill3 = calculate_tip(750, 18)

print("Bill 1:", bill1)
print("Bill 2:", bill2)
print("Bill 3:", bill3)