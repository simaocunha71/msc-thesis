
The code you have written is not working as expected. The logic for the code seems to be correct but there are few things you need to fix:

1. You are not importing fmt package which is needed for Println function.
2. You are not handling the negative numbers and numbers greater than 9.

Here is the correct code:

```go
import  (
    "sort"
    "fmt"
)

func ByLength(arr []int) []string {
    // Remove numbers outside the range 1-9
    var validNums []int
    for _, num := range arr {
        if num >= 1 && num <= 9 {
            validNums = append(validNums, num)
        }
    }

    sort.Ints(validNums