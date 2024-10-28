

def truncate_number(number: float) -> float:
    integer_part, decimals = math.modf(number)
    return decimals
