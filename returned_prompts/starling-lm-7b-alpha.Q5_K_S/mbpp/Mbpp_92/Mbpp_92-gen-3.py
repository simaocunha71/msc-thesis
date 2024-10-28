
def is_undulating(num: int) -> bool:
    return num%10 != 0 and num%(num//10) == 0


