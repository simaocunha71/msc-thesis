def check_smaller(tuple1, tuple2):
    for i, j in zip(tuple1, tuple2):
        if i >= j:
            return False
    return True