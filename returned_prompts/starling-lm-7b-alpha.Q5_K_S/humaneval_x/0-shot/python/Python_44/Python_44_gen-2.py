

def change_base(x: int, base: int):
    # convert to string
    s = str(x)
    # convert to base
    s = bin(int(s, 10))[2:].zfill(base)
    # convert to int
    return int(s, base)


# testing
print(change_base(8, 3))
print(change_base(8, 2))
print(change_base(7, 2))






# Made By Mostafa_Khaled
# Python Egypt
# Noob Programmer
# Ain't no one can beat me:D
# I'll see you in the next question !!!


```