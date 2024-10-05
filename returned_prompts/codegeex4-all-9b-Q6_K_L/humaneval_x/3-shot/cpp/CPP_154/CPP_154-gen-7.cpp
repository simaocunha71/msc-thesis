
has_close_elements()
Your algorithm is correct, but it is not optimal for large vectors.  The complexity is O(n^2), which is not ideal.  You can improve this by using a set to store the numbers and then checking the distance to the nearest number in the set.  This would be O(n log n) complexity.
separate_paren_groups()
The code is correct, but it is not very efficient.  You are using a string to build the current_paren string, which can be inefficient.  Instead, you should use a stringstream.  Also, you do not need to check if level is 0 when adding the current_paren to all_parens.  This can be done after the loop.
truncate_number()
The code is correct, but it can be simplified.  You can use the fmod function to get the fractional part of the number.
cycpattern_check()
The code is correct, but it can be simplified.  You can use the find function with the second argument to start the search from the position after the last match.  Also, you do not need to create a new string for b in each iteration of the loop.  You can use substr to get the substring.
Overall
The code is well-structured and follows good coding practices.  However, there are some areas where it can be improved.  I hope these suggestions are helpful.