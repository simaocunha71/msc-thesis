    import math

    def max_fill(grid, capacity):
        """
        Calculate the maximum number of times a bucket needs to be lowered to empty all wells,
        given that the capacity of the bucket is equal to the parameter provided.
        """
        # Calculate the sum of all wells
        well_sum = sum(sum(row) for row in grid)

        # Calculate the number of times a bucket needs to be lowered,
        # given that the total sum of all wells is divisible by the bucket's capacity
        return math.ceil(well_sum / capacity)




# tests

def test_max_fill():
    assert max_fill([[0, 0, 1, 0], [0, 1, 0, 0], [1, 1, 1, 1]], 1) == 6
    assert max_fill([[0, 0, 1, 1], [0, 0, 0, 0], [1, 1, 1, 1], [0, 1, 1, 1]], 2) == 5
    assert max_fill([[0, 0, 0], [0, 0, 0]], 5) == 0


def test_truncate_number():
    assert truncate_number(3.5) == 0.5


def test_separate_paren_groups():
    assert separate_paren_groups('( ) (( )) (( )( ))') == ['()', '(())', '(()())']


def test_has_close_elements():
    assert has_close_elements([1.0, 2.0, 3.0], 0.5) == False
    assert has_close_elements([1.0, 2.8, 3.0, 4.0, 5.0, 2.0], 0.3) == True


if __name__ == "__main__":
    test_max_fill()
    test_truncate_number()
    test_separate_paren_groups()
    test_has_close_elements()

# Made by Sphinx