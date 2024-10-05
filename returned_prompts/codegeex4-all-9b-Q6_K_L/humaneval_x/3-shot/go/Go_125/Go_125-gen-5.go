
Your first function is correct.
Your second function has a small issue: if the string ends with an open parenthesis, you will not add it to your results. You should add a check at the end of your loop to see if you're at the last element and if it's an open parenthesis, then you should add it.
Your third function has a small issue: if the number is a whole number, you will return 0.0 instead of 0. You should return 0 instead of 0.0.
Your fourth function has a small issue: if the string contains neither a space nor a comma, you will return the count of lower-case letters with odd order in the alphabet, but you should return the count of lower-case letters with odd order in the alphabet, or the string split on whitespace if it contains a space, or the string split on comma if it contains a comma.

Here's the corrected code:
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

    if len(current_string) > 0 {
        result = append(result, string(current_string))
    }

    return result
}

func TruncateNumber(number float64) float64 {
    return math.Mod(number, 1)
}

func SplitWords(txt string) interface{} {
    if strings.Contains(txt, " ") {
        return strings.Split(txt, " ")
    } else if strings.Contains(txt, ",") {
        return strings