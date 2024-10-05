
There is a problem with the following line of your code:
current_string =  make([]rune, 0)

This line will create a new slice with length 0, but capacity of len(current_string). This is probably not what you intended. You probably want to create a new slice with length and capacity of 0, like this:
current_string =  make([]rune, 0, 0)

However, this is not the only problem with your code. The function SeparateParenGroups has a number of logical errors:

If the input string does not have a balanced number of parentheses, the function will panic when it tries to append a closing parenthesis to the current_string slice.
The function does not check if the input string contains any spaces. It should skip spaces when iterating over the characters in the string.
The function does not check if the input string contains any characters that are not parentheses or spaces. It should ignore any other characters when iterating over the characters in the string.

Here is a corrected version of the SeparateParenGroups function:
func SeparateParenGroups(paren_string string) []string {
    result := make([]string, 0)
    current_string := make([]rune, 0)
    current_depth := 0

    for _, c := range paren_string {
        if c == '(' {
            current_depth += 1
            current_string = append(current_string, c)
        } else if c == ')' {
            current_depth -= 1
            current_string = append(current_string, c)

           