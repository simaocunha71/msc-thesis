    def rotate_string(s: str, times: int) -> str:
        return s[times:] + s[:times]

    if a == b:
        return True
    elif len(a) < len(b):
        return False
    else:
        for i in range(len(b)):
            if b in a:
                return True
            else:
                a = rotate_string(a, 1)
        return False


