def predict_next_number(prev_number, prev_diff):
    next_number = ""
    for i, digit in enumerate(prev_number):
        next_digit = (int(digit) + prev_diff[i]) % 10  # Basic increment with wrap around
        next_number += str(next_digit)
    return next_number

# Previous numbers and their differences
prev_number = "5388957939970072"
current_number = "5278806585486127"
prev_diff = [int(current_number[i]) - int(prev_number[i]) for i in range(16)]

# Predict the next number
next_identifier = 6123
next_number = predict_next_number(current_number, prev_diff)

print(f"Next number: {next_number} ({next_identifier})")