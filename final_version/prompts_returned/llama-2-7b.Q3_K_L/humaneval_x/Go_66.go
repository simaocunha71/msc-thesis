
// Task
// Write a function that takes a string as input and returns the sum of the upper characters only'
// ASCII codes.
// 
// Examples:
// Digitsum("") => 0
// Digitsum("abAB") => 131
// Digitsum("abcCd") => 67
// Digitsum("helloE") => 69
// Digitsum("woArBld") => 131
// Digitsum("aAaaaXa") => 153
func Digitsum(x string) int {
    var total = 0
    for i := range x {
        if (((i + 1) < len(x)) && !isLetter(x[i + 1])) {
            total += x[i] - 'a'
        } else {
            break
        }
    }
    return total
}

// isLetter returns true if the character is a letter in lowercase or title case.
func isLetter(c rune) bool {
    return !((('a' <= c) && (c <= 'z')) || ('A' <= c && (c <= 'Z')))
}
