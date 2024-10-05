Here is the solution in Go:
```go
import (
    "fmt"
)

func OddCount(lst []string) []string {
    result := make([]string, len(lst))
    for i, s := range lst {
        count := 0
        for _, c := range s {
            if c % 2 != 0 {
                count++
            }
        }
        result[i] = fmt.Sprintf("the number of odd elements %dn the str%dng %d of the %dnput.", count, i+1, i+1, i+1)
    }
    return result
}
```
Here is how it works:
1. Create a new slice `result` with the same length as `lst`.
2. Iterate over each string `s` in `lst`.
3. Count the number of odd