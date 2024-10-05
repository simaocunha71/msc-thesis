    import re
    # Extract numbers from the input string
    numbers = list(map(int, re.findall(r'\d+', s)))

    # Calculate the total number of mangoes
    mangoes = n - sum(numbers)

    return mangoes

