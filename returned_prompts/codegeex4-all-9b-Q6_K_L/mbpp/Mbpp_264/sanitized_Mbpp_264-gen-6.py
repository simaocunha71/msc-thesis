def dog_age(dog_years: int) -> int:
    """Calculate a dog's age in dog's years."""
    if dog_years < 2:
        return 10 * dog_years
    else:
        return 10 * 2 + 4 * (dog_years - 2)