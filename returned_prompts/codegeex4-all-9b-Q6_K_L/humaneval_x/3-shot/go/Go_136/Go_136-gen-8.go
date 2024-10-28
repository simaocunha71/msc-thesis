
for _, c := range paren_string {

You're iterating over every character in the string, not every character in the string that represents a parenthesis.
Instead of:
for _, c := range paren_string {

Use:
for i, c := range paren_string {

Then, check if the character is a parenthesis:
if c == '(' || c == ')' {

Finally, you can use the index i to determine the depth of the parentheses. If the character is an open parenthesis, increase the depth by 1. If the character is a closing parenthesis, decrease the depth by 1.
if c == '(' {
    current_depth += 1
} else if c == ')' {
    current_depth -= 1
}

Then, when the depth is 0, you can add the current string to the result:
if current_depth == 0 {
    result = append(result, string(current_string))
    current_string = []rune{}
}

Here's a corrected version of your SeparateParenGroups function:
func SeparateParenGroups(paren_string string) []string {
    result := []string{}
    current_string := []rune{}
    current_depth := 0

    for i, c := range paren_string {
        if c == '(' || c == ')' {
            current_string = append(current_string, c)
            if c == '(' {
                current_depth += 1
            } else {
                current_depth -= 1
            }

            if current_depth == 0 {
                result = append(result, string(current_string))
                current_string = []rune{}
            }
        }
    }

    return result
}