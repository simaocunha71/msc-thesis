return any(abs(n1 - n2) <= threshold for n1 in numbers for n2 in numbers if n1 != n2)
