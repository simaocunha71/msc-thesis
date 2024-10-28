
Your code looks good, you have implemented the given requirements correctly. Here are a few minor points that could potentially be improved:

In HasCloseElements, you could avoid checking the same pairs of numbers twice by starting the inner loop from i + 1 instead of 0.
In SeparateParenGroups, you could use a for range loop to iterate over the string, which would be more idiomatic in Go. Also, you could use a slice instead of a rune slice for current_string, as you are only appending single characters.
In TruncateNumber, you could use the math.Floor function to get the integer part of the number, and then subtract it from the original number to get the decimal part.
In FixSpaces, you could use strings.ReplaceAll instead of strings.Replace to replace all occurrences of a substring in a string.
Overall, your code is well-structured and easy to understand, and you have implemented the given requirements correctly.