
The first one is good.
The second one is a little bit convoluted. You can simplify it by using a stack. When you encounter a parenthesis, just push it to the stack, and when you encounter a closing parenthesis, pop it from the stack. If the stack is empty after popping, then you found a group.
For example:
func SeparateParenGroups(paren_string string) []string {
    var result []string
    var stack []rune
    var current_string []rune

    for _, c := range paren_string {
        if c == '(' {
            stack = append(stack, c)
            current_string = append(current_string, c)
        } else if c == ')' {
            stack = stack[:len(stack)-1]
            current_string = append(current_string, c)

            if len(stack) == 0 {
                result = append(result, string(current_string))
                current_string = make([]rune, 0)
            }
        }
    }
    return result
}

The third one is also a good one. The fourth one is also good, but you can simplify it by using regular expressions. For example:
func FruitDistribution(s string, n int) int {
    re := regexp.MustCompile(`(\d+) apples and (\d+) oranges`)
    match := re.FindStringSubmatch(s)
    apples, _ := strconv.Atoi(match[1])
    oranges, _ := strconv.Atoi(match[2])
    return n - apples - oranges
}