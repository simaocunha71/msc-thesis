
You're on the right track. However, there are a few things that can be improved:

1. You should use a switch statement instead of multiple if-else statements. This will make the code more readable and easier to maintain.
2. You don't need to check if the current depth is 0 before appending the current string to the result. You can do this in the else case.
3. You should use the append function to add elements to the result and current_string slices. This will make the code more readable and easier to maintain.
4. You should use the range loop to iterate over the parentheses string. This will make the code more readable and easier to maintain.
5. You should use the strings package to remove spaces from the input string. This will make the code more readable and easier to maintain.

Here's an updated version of your code:

func SeparateParenGroups(paren_string string) []string {
    result := make([]string, 0)
    current_string := make([]rune, 0)
    current_depth := 0

    paren_string = strings.ReplaceAll(paren_string, " ", "")

    for _, c := range paren_string {
        switch c {
        case '(':
            current_depth += 1
            current_string = append(current_string, c)
        case ')':
            current_depth -= 1
            current_string = append(current_string, c)

            if current_depth == 0 {
                result = append(result, string(current_string))
                current_string = make([]rune, 0)
            }
        }
    }

    return result
}