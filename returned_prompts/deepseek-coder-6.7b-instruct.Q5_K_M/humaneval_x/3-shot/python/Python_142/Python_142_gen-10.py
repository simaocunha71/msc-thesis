    return sum(el**2 if i%3==0 else el**3 if i%4==0 and i%3 != 0 else el for i, el in enumerate(lst))


