Here is the solution:

```go
import (
    "fmt"
)

func OddCount(lst []string) []string {
    result := make([]string, len(lst))
    for i, str := range lst {
        count := 0
        for _, c := range str {
            if c%2 != 0 {
                count++
            }
        }
        result[i] = fmt.Sprintf("the number of odd elements %dn the str%dg of the %dnput.", count, i+1, i+1)
    }
    return result
}
```

In this solution, we iterate over each string in the input list and for each string, we iterate over each character (digit). If the digit is odd, we increment the count. We then format the result string using the count and the string index. The `fmt.Sprintf` function is used to format the string, and the `%d` format specifier is used to replace the count with the actual value.

The resulting list of strings is then returned. This solution has a time complexity of O(n*m), where n is the length of the input list and m is the length of the longest string in the list, since we are iterating over each character in each string. The space complexity is O(n), since we are storing the result in a list of strings.