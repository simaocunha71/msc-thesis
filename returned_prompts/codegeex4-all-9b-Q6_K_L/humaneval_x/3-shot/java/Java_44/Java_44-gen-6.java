
Your hasCloseElements function is correct, and works in O(n^2) time. There are faster solutions, but they're not much more efficient than this one, and they're more complicated.
Your separateParenGroups function is almost correct. It fails in the case where there are no groups of parentheses. This could be fixed by initializing current_depth to 1, and modifying the if (current_depth == 0) check to if (current_depth == 1).
Your truncateNumber function is correct.
Your changeBase function is correct.