
Imports
You have three different packages you import. It's not really bad, but you don't use anything from the math package, so you might as well remove it.
Also, the strings package has a Reverse function that you can use instead of reversing the string manually.
Overall, I'd remove the math package and rename the strings package to s.
Variable Names
You have a lot of single-character variable names, which isn't really bad, but it's hard to understand what they are. For example, i and j in HasCloseElements are hard to understand. You could use index1 and index2 instead.
Also, in SeparateParenGroups, current_string is a bit confusing. You're using it to store the current group, but it's not really a string, it's a slice of runes. I'd rename it to current_group.
Return Types
Your SeparateParenGroups function returns a slice of strings, but it also returns a boolean. This is fine, but it's a bit unconventional. You might want to consider returning a slice of bools instead, or a struct that contains both the slice of strings and the boolean.
Also, in ReverseDelete, you return a tuple of a string and a boolean. I'd suggest returning a struct that contains both the string and the boolean, or a slice of bools that contains both the boolean and the boolean.
HasCloseElements
Your HasCloseElements function is fine, but it could be more efficient. Instead of comparing each pair of numbers, you could sort the slice and then check for any two adjacent numbers that are closer than the threshold.
SeparateParenGroups
Your SeparateParenGroups function is fine, but it could be more efficient. Instead of iterating over each character in the input string, you could use a stack to keep track of the current group.
TruncateNumber
Your TruncateNumber function is fine, but it could be more efficient. Instead of using math.Mod, you could use a bit shift to calculate the integer part and then subtract it from the original number.
ReverseDelete
Your ReverseDelete function is fine, but it could be more efficient. Instead of using strings.ReplaceAll, you could use