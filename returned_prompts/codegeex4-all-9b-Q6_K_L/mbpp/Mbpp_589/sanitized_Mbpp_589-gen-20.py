def perfect_squares(start_num: int,end_num: int) -> list:
    perfect_squares = [i for i in range(start_num, end_num+1) if i**0.5 == int(i**0.5)]
    return perfect_squares