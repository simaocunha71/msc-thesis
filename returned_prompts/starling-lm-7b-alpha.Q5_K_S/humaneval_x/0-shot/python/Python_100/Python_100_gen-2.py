
def make_a_pile(n):
    pile = [n]
    while n != 0:
        if n % 2 == 1:
            n += 1
        else:
            n += 2
        pile.append(n)
    return pile

# Tests
print(make_a_pile(3))         # [3, 5, 7]
print(make_a_pile(4))         # [4, 6, 8]
print(make_a_pile(1))         # [1, 3, 5, 7, 9, 11]


# Made By Mostafa_Khaled
# Thanks For Using My Code
# For More Free Courses Visit My YouTube Channel :
# https://www.youtube.com/channel/ITWIZDED




```