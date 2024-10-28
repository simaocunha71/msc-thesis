def dog_age(years):
    dog_years = 0
    for year in range(years):
        if year < 2:
            dog_years += 1
        else:
            dog_years += 2
    return dog_years