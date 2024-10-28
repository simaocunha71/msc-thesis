def dog_age(human_years):
    if human_years < 1:
        return 0
    elif human_years < 2:
        return 14
    else:
        return 14 + (human_years - 2) * 10