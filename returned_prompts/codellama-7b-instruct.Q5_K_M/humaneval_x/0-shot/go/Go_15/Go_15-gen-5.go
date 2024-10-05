import (
    "strconv"
    "strings"
)

// Return a string containing space-delimited numbers starting from 0 upto n inclusive.
// >>> StringSequence(0)
// '0'
// >>> StringSequence(5)
// '0 1 2 3 4 5'
func StringSequence(n int) string{
    var result string
    for i := 0; i <= n; i++{
        result += strconv.Itoa(i) + " "
    }
    return strings.TrimSpace(result)
}
