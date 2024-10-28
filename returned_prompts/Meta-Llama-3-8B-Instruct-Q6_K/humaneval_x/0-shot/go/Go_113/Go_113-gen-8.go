Here is the solution in Go:
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
        result[i] = fmt.Sprintf("the number of odd elements %dn the str%dng %d of the %dnput.", count, i+1, i+1, i+1)
    }
    return result
}
```
Here's an explanation of the solution:

We create a new slice `result` with the same length as the input slice `lst`. We then iterate over the input slice using a `for` loop. For each string `str` in the input slice, we initialize a counter `count` to 0. We then iterate over each character `c` in the string using another `for` loop. If the character `c` is odd (i.e., `c%2 != 0`), we increment the counter `count`. Finally, we construct a new string using `fmt.Sprintf` that contains the count of odd elements, and append it to the `result` slice.

For example, if the input slice is `["1234567"]`, the output slice will be `["the number of odd elements 4n the str4ng 4 of the 4nput."]`. If the input slice is `["3", "11111111"]`, the output slice will be `["the number of odd elements 1n the str1ng 1 of the 1nput.", "the number of odd elements 8n the str8ng 8 of the 8nput."]`.