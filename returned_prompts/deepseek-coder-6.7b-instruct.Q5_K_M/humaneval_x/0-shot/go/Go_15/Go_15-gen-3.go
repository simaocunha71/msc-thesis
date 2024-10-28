import (
    "strconv"
    "strings"
)

// Return a string containing space-delimited numbers starting from 0 upto n inclusive.
// 
// 
// 
// 
func StringSequence(n int) string{
    var result []string
    for i := 0; i <= n; i++ {
        result = append(result, strconv.Itoa(i))
    }
    return strings.Join(result, " ")
}




