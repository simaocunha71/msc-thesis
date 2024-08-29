
def round_and_sum(numbers):
    round_numbers = [round(i) for i in numbers]
    total = sum(round_numbers)
    return total * len(numbers)

print(round_and_sum([22.4, 4.0, -16.22, -9.10, 11.00, -12.22, 14.20, -5.20, 17.50]))
<jupyter_output>
243
<jupyter_text>
Problem 3
<jupyter_code>
