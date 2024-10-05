Here is a simple solution in Go:
```go
import (
    "strconv"
)

func EvenOddCount(num int) [2]int {
    evenCount := 0
    oddCount := 0
    str := strconv.Itoa(num)
    for _, c := range str {
        digit, _ := strconv.Atoi(string(c))
        if digit%2 == 0 {
            evenCount++
        } else {
            oddCount++
        }
    }
    return [2]int{evenCount, oddCount}
}
```
Here's an explanation of the code:

1. We convert the integer `num` to a string using `strconv.Itoa`.
2. We initialize two counters, `evenCount` and `oddCount`, to 0.
3. We iterate over each character `c` in the string using a range loop.
4. For each character, we convert it to an integer using `strconv.Atoi` and store it in the `digit` variable.
5. We check if the digit is