    eaten = number + (need - number)
    remaining = max(0, remaining - (need - number))
    return [eaten, remaining]  # or return [eaten, remaining] for better readability


