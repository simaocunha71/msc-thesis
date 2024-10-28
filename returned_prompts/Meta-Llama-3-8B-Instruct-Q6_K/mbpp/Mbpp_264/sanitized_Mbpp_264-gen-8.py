def dog_age(human_age):
    if human_age < 1:
        return "Invalid input"
    elif human_age < 2:
        return 14
    else:
        return human_age * 7 + 2.5