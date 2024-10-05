    # your code here
    if n < 4:
        return False
    if n % 2 == 1:
        return False
    for i in range(2, n//2 + 1):
        if (i * 4) % 2 == 1:
            continue
        if n % (i * 4) == 0:
            return True
    return False


































# In the game of Connect Four, each 7x6 board is divided into 35 columns. Each column can have 6 rows. Each row can have a red or black piece. This means there are 2^35 possible board states. However, not all of these states are valid. A valid board state is one where no four consecutive pieces of the same color appear in a row, column, or diagonal.

# For example, the following are valid board states:

# connect_four_states(1) == []
# connect_four_states(2) == [0, 1]
# connect_four_states(3) == [0, 1, 2]
# connect_four_states(4) == [0, 1, 2, 3]
# connect_four_states(5) == [0, 1, 2, 3, 4]
# connect_four_states(6) == [0, 1, 2, 3, 4, 5]
# connect_four_states(7) == [0, 1, 2, 3, 4, 5, 6]
# connect_four_states(8) == []
# connect_four_states(9) == [0, 1, 2, 3, 4, 5, 6]
# connect_four_states(10) == [0, 1, 2, 3, 4, 5, 6, 7]
# connect_four_states(11) == [0, 1, 2, 3, 4, 5, 6, 7, 8]

# Here are some invalid