def dog_age(years):
    years = years
    dog_years = 0
    while years > 0:
        if years > 10:
            dog_years += 10
            years -= 10
        else:
            dog_years += years
            years = 0
    return dog_years