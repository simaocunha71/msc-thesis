
You have some good answers in this thread but I wanted to add a few more things.
Firstly, I want to address some of the questions you asked in comments on other answers.  You said that you didn't understand why the HasCloseElements function was O(n^2).  The reason is that your function has two nested loops: the outer loop runs n times and for each iteration of the outer loop, the inner loop runs up to n times.  Thus, the total number of iterations is n*n which is O(n^2) or quadratic time complexity.
You also asked why the SeparateParenGroups function was O(n).  The reason is that it has a single loop that iterates through the input string exactly once.  Thus, the time complexity is linear or O(n).
Regarding the SeparateParenGroups function, I would like to point out that the code is inefficient.  It uses a slice of runes to build the current_string and then converts it to a string before appending it to the result.  This is unnecessary and can be avoided by using a single string instead of a slice of runes.  Here is an improved version of the function:
func SeparateParenGroups(paren_string string) []string {
    result := make([]string, 0)
    current_string := ""
    current_depth := 0

    for _, c := range paren_string {
        if c == '(' {
            current_depth += 1
            current_string += string(c)
        } else if c == ')' {
            current_depth -= 1
            current_string += string(c)

            if current_depth == 0 {
                result = append(result, current_string)
                current_string = ""
            }
        }
    }
    return result
}

Finally, I want to point out that the TruncateNumber function is incorrect.  The math.Mod function returns the remainder of the division, which is not what you want.  You want to return the fractional part of the number, which is the number minus its integer part.  Here is a corrected version of the