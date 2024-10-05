
Q1: has_close_elements
Your code looks good.  I only have one comment.  It is not necessary to declare the loop variable i and j inside the loop.  It is good practice to declare variables in the smallest scope possible.  In this case, it can be done in the for statement.
Q2: separate_paren_groups
Your code looks good, but there is one problem.  If the input string ends in a parenthesis without another parenthesis before it, the last group will be missing.  To fix this, you can add a check at the end of the loop to add any remaining parenthesis to the current group before adding it to the vector.
Q3: truncate_number
Your code looks good.  It is a simple calculation.
Q4: modp
Your code looks good, but there is one problem.  If n is 0, the result will be 0.  If n is not divisible by p, the result will be the remainder.  To fix this, you can return 1 if n is 0, and n % p if n is not divisible by p.
Overall, your code looks good.  It is well-organized and easy to read.  The only comments I have are about the scope of variables and one problem with the separate_paren_groups function.