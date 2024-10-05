import (
    "strconv"
)

// Return a string containing space-delimited numbers starting from 0 upto n inclusive.
// >>> StringSequence(0)
// '0'
// >>> StringSequence(5)
// '0 1 2 3 4 5'
func StringSequence(n int) string{
    var b strings.Builder
    for i := 0; i <= n; i++ {
        b.WriteString(strconv.Itoa(i))
        b.WriteString(" ")
    }
    return b.String()
}

