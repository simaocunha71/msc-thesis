def is_decimal(num: str) -> bool:
    try:
        float(num)
        return True
    except ValueError:
        return False