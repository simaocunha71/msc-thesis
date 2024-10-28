
has_close_elements

You're using abs which is a common function in the math library, but you forgot to include it. It's not that big of a deal, but it's a good habit to include all necessary headers.

Your function is currently O(n^2), which is not optimal. You can reduce it to O(n) by using a std::map to store the numbers. This way you can simply iterate through the map and compare the distance of each number to the next.

separate_paren_groups

You're using a char variable when you could use a char. It's a minor change, but it's a good practice to be as precise as possible.

You're using a for loop with i as the loop variable, but you're not actually using i. This is not a big deal, but it's a good practice to use the loop variable.

Your function is currently O(n^2), which is not optimal. You can reduce it to O(n) by using a std::stack. This way you can simply iterate through the string and push and pop parentheses as needed.

truncate_number

You're using int(number) which is not a good practice. The correct way to truncate a number is to use std::floor or std::ceil.

total_match

You're using a for loop with i as the loop variable, but you're not actually using i. This is not a big deal, but it's a good practice to use the loop variable.

Your function is currently O(n^2), which is not optimal. You can reduce it to O(n) by using a single loop to calculate the total number of characters in each list. This way you can simply compare the two totals in a single operation.

Overall, these are some of the main issues I see with your code. If you have any more questions, feel free to ask.