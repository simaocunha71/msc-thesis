
Overall, your solutions look good and should work as expected. They follow a clear and logical structure, with comments explaining the purpose of each function and the logic behind the calculations. 

However, there is a small issue in the SeparateParenGroups function. The code currently checks if the current depth is 0 after every closing parenthesis, which means it will add an empty string to the result slice if there are consecutive closing parentheses. To fix this, you should check if the current depth is 0 only after the innermost parentheses are closed. Here's the corrected version:

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

            if current_depth == 0 {
                result = append(result, string(current_string))
                current_string = make([]rune, 0)
            }
        }
    }

    return result
}

Additionally, you might want to add some error handling for cases where the input string is not a valid representation of nested parentheses. For example, you can check if the number of opening parentheses matches the number of closing parentheses:

func SeparateParenGroups(paren_string string) ([]string, error) {
    result := make([]string, 0)
    current_string := make([]rune, 0)
    current_depth := 0

    for _, c := range paren_string {
        if c == '(' {
            current_depth += 1
            current