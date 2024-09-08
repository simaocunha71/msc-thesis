def validate(n):
    num_dict = {}
    for digit in str(n):
        if digit in num_dict:
            num_dict[digit] += 1
        else:
            num_dict[digit] = 1
    
    for digit, count in num_dict.items():
        if count > int(digit):
            return False
    return True