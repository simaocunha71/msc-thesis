    def rotate(string, n):
        return string[n:] + string[:n]

    for i in range(len(b)):
        rotated_b = rotate(b, i)
        if rotated_b in a:
            return True
    return False

