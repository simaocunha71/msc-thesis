
The first question is a simple O(n^2) search to find two elements that are within the given threshold of each other.
There are faster ways to do this, but they require additional space to store the elements.
For example, you could use a HashSet to store the elements, and then iterate through the HashSet to find two elements that are within the threshold of each other. This would be O(n) in time and O(n) in space.

The second question is a bit more complex. You need to iterate through the string and keep track of the current depth of parentheses. If you encounter an open parenthesis, you increase the depth by 1. If you encounter a close parenthesis, you decrease the depth by 1. If the depth is 0 after encountering a close parenthesis, you add the current string to the result list and reset the current string.
This is a simple problem that can be solved with a single pass through the string and constant space.

The third question is a simple arithmetic problem. The decimal part of a number is the number minus the integer part of the number. The integer part of a number is the largest integer smaller than the number. This can be done with a single line of code.

The fourth question is a bit more complex. You need to check that the date string is in the correct format, and that the month and day are within the correct range. You also need to check that the year is not negative.
This can be done with a simple if statement and a few lines of code.