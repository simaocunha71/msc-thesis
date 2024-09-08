def get_ludic(n):
    def is_ludic(num):
        digits = [int(d) for d in str(num)]
        return sum(digits) == len(digits)
    
    return [i for i in range(1, n+1) if is_ludic(i)]