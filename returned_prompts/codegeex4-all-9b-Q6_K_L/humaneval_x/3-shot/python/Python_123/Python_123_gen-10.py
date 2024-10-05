    collatz_sequence = []
    current_number = n

    while current_number != 1:
        collatz_sequence.append(current_number)

        if current_number % 2 == 0:
            current_number //= 2
        else:
            current_number = 3 * current_number + 1

    collatz_sequence.append(1)

    odd_numbers = [num for num in collatz_sequence if num % 2 != 0]

    return odd_numbers

