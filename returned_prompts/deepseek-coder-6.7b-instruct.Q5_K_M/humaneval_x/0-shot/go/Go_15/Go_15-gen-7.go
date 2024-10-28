    result := ""
    for i:=0; i <= n; i++ {
        result += strconv.Itoa(i) + " "
    }
    return result
}
*/

import (
	"strconv"
	"strings"
)

// StringSequence returns a string containing space-delimited numbers starting from 0 upto n inclusive.
func StringSequence(n int) string {
	var sb strings.Builder
	for i := 0; i <= n; i++ {
		sb.WriteString(strconv.Itoa(i))
		if i < n {
			sb.WriteRune(' ')
		}
	}
	return sb.String()
}

// StringSequenceUsingSprintf is another implementation using Sprintf
func StringSequenceUsingSprintf(n int) string {
	var str string
	for i := 0; i <= n; i++ {
		str += fmt.Sprintf("%d ", i)
	}
	return strings.TrimSpace(str)
}

// StringSequenceUsingJoin is another implementation using strings.Join and strconv.Itoa
func StringSequenceUsingJoin(n int) string {
	str := make([]string, n+1)
	for i := range str {
		str[i] = strconv.Itoa(i)
	}
	return strings.Join(str, " ")
}

// StringSequenceUsingFormatf is another implementation using fmt.Sprintf
func StringSequenceUsingFormatf(n int) string {
	str := ""
	for i := 0; i <= n; i++ {
		str += fmt.Sprintf("%d ", i)
	}
	return strings.TrimSpace(str)
}

// StringSequenceUsingBuffer is another implementation using bytes.Buffer
func StringSequenceUsingBuffer(n int) string {
	var buf bytes.Buffer
	for i := 0; i <= n; i++ {
		buf.WriteString(strconv.Itoa(i))
		if i < n {
			buf.WriteByte(' ')
		}
	}
	return buf.String()
}

// StringSequenceUsingBuilder is another implementation using strings.Builder
func StringSequenceUsing