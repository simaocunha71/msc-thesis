
You have a lot of good questions here. Here's a few comments on your code:

Your hasCloseElements method has a very bad time complexity. The current implementation is O(n^2). You can improve this to O(n) by sorting your numbers first, and then checking if the difference between any two adjacent numbers is less than the threshold.

Your separateParenGroups method is not quite correct. It will not work for inputs with nested parentheses, as it assumes that each group of parentheses is a separate group. You should instead count the depth of the parentheses, and start a new group when the depth returns to zero.

Your truncateNumber method is correct, but you can simplify it by using Math.floorMod instead of subtracting 1.0.

Your strangeSortList method is correct, but it can be simplified by using a deque and a boolean flag to keep track of whether you should add the minimum or maximum next.

Overall, your code is very good. You have a good understanding of Java and the programming concepts you're learning. Keep up the good work!