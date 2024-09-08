def power_base_sum(base, power):
    total_sum = 0
    current_number = base
    for _ in range(power):
        total_sum += sum(int(digit) for digit in str(current_number))
        current_number *= base
    return total_sum