    return sorted([x for x in x if all(int(digit) % 2 != 0 for digit in str(x))])  # sorted list of elements that haven't any even digit


