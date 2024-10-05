# Here is one possible solution.
def make_a_pile(n):
    pile = [n]
    while pile[-1] % 2 == 0:
        pile.append(pile[-1] + 2)
    while pile[-1] % 2 == 1:
        pile.append(pile[-1] + 3)
    return pile

# Here's a possible unit test.
def test_make_a_pile():
    assert make_a_pile(3) == [3, 5, 7]
    assert make_a_pile(4) == [4, 6, 8, 10]
    assert make_a_pile(5) == [5, 7, 9, 11, 13]
    assert make_a_pile(6) == [6, 8, 10, 12, 14]
    assert make_a_pile(7) == [7, 9, 11, 13, 15, 17]
    assert make_a_pile(8) == [8, 10, 12, 14, 16, 18]
    assert make_a_pile(9) == [9, 11, 13, 15, 17, 19, 21]
    print("All tests passed.")

test_make_a_pile()



































































































































































