
Your second function is correct. You have a good understanding of how to handle strings and characters in Go.
Here's the code with minor improvements:
func SeparateParenGroups(paren_string string) []string {
    result := make([]string, 0)
    current_string := make([]rune, 0)
    current_depth := 0

    for _, c := range paren_string {
        switch c {
        case '(':
            current_depth++
            current_string = append(current_string, c)
        case ')':
            current_depth--
            current_string = append(current_string, c)

            if current_depth == 0 {
                result = append(result, string(current_string))
                current_string = make([]rune, 0)
            }
        }
    }
    return result
}

This version uses a switch statement to handle the cases of '(' and ')', which makes the code easier to read and maintain.

Your third function is also correct, but you can improve its readability by using a map to check if a character is a vowel:
func VowelsCount(s string) int {
    s = strings.ToLower(s)
    count := 0
    vowels := map[rune]bool{
        'a': true,
        'e': true,
        'i': true,
        'o': true,
        'u': true,
    }

    for _, c := range s {
        if vowels[c] {
            count++
        }
    }

    if s[len(s)-1] == 'y' {
        count++
    }

    return count
}

This version uses a map to store the vowels, which makes the code more concise and easier to understand.