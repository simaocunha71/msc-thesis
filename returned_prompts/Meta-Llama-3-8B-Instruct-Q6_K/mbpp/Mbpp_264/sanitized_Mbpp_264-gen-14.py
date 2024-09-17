def dog_age(human_age):
    if human_age < 0:
        raise ValueError("human_age must be a positive integer")
    if not isinstance(human_age, int):
        raise TypeError("human_age must be an integer")
    return 7*human_age