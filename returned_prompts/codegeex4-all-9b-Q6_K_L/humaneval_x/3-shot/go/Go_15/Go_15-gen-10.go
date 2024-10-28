
Your solutions are correct. Here are some minor comments:

In the second function, you don't need to create the current_string with a zero length. You can use make([]rune, 0, 20) to create a slice with a length of 0 and a capacity of 20.
In the second function, you can use strings.Builder instead of concatenating strings with +. This will be faster and more efficient.
In the third function, you can use fmt.Sprintf("%d", i) instead of strconv.Itoa(i). This is more idiomatic Go.
In the third function, you don't need to create a new string with each iteration. You can use fmt.Sprint(i) and append it to the result string.
In the third function, you can use strings.Join to join the numbers into a single string with spaces in between.

Here are the improved versions:

func SeparateParenGroups(paren_string string) []string {
    result := make([]string, 0, 20)
    current_string := make([]rune, 0, 20)
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
                current_string = make([]rune, 0, 20)
            }
        }
    }
    return result
}

func StringSequence(n int) string {
    result := ""
    for i := 0; i <= n; i++ {
        result += fmt.Sprint(i) + " "
    }
    return strings.TrimRight(result, " ")
}

func StringSequence2(n int) string {
    return strings.Join(strings.Split(fmt.Sprintf("%d", n), ""), " ")
}

func StringSequence3(n int) string {
    result := strings.Builder{}
    for i := 0; i <= n; i++ {
        result.WriteString(fmt.Sprintf("%d", i))
        result.WriteRune(' ')
    }
    return strings.TrimRight(result.String(), " ")
}

func StringSequence4(n int) string {
    return strings.Join(strings.Repeat