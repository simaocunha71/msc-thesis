
Your code is well written. It is neat and readable, and you use idiomatic Go constructs. I have a few minor comments:

In HasCloseElements, you could use range instead of manual indexing to iterate over the slice.
In SeparateParenGroups, you could use a bytes.Buffer to build the strings instead of appending to a slice of runes. This would be more efficient, as it avoids the overhead of allocating a new slice for each append.
In TruncateNumber, you could use math.Trunc instead of math.Mod to truncate the number.
In ParseNestedParens, you could use a for range loop to iterate over the string, and you could use a bytes.Buffer to build the strings instead of appending to a slice of runes. You also don't need to reset current_depth and max_depth to 0 after appending to result. The next iteration will start with a new group of parentheses.
In ParseNestedParens, you could use a flag to indicate when to start building a string, and you could use a flag to indicate when to append a string to result. This would make the code more readable, as you wouldn't have to check the current_depth and max_depth in multiple places.
In ParseNestedParens, you could use a flag to indicate when to reset current_depth and max_depth. This would make the code more readable, as you wouldn't have to check the current_depth and max_depth in