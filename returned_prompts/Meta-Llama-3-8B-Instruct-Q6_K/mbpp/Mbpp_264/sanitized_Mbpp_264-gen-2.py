def dog_age(years):
    human_years = 0
    while years > 0:
        if years > 2:
            human_years += 3
            years -= 2
        else:
            human_years += years
            years = 0
    return human_years