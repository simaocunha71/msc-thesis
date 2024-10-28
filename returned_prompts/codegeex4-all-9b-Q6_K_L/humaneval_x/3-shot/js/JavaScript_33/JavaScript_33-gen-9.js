
hasCloseElements
You don't need to loop through every pair of numbers. You can use Math.min and Math.max to find the smallest and largest number, and then just check if the difference between those two numbers is less than the threshold.
This can be done in O(n) time, where n is the number of elements in the array, which is more efficient than your current solution.

separateParenGroups
Your solution is correct, but it can be made more efficient by keeping track of the current depth in a single loop, rather than incrementing and decrementing a counter. This can be done by counting the number of open parentheses and checking if it's 0 when a closing parenthesis is encountered.
This can also be done in O(n) time.

truncateNumber
Your solution is correct, but it can be simplified to just return number - Math.floor(number).

sortThird
Your solution is correct, but it can be made more efficient by using a single loop to find the indices and values of the elements to be sorted, and then using Array.sort to sort them. This can be done in O(n log n) time, where n is the number of elements in the array, which is more efficient than your current solution.