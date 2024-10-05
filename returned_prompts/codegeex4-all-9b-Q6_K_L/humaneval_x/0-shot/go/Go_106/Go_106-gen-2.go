
Here is a simple implementation of the function F in Go:

```go
import "math"

func F(n int) []int {
    result := make([]int, n)
    for i := 1; i <= n; i++ {
        if i % 2 == 0 {
            result[i-1] = int(math.Pow(float64(i), 2))
        } else {
            result[i-1] = i * (i + 1) / 2
        }
    }
    return result
}
```

In this function, we first initialize a slice of size n to store the result. Then, we iterate from 1 to n. If the current index i is even, we calculate the square of i and store it in the result slice. Otherwise, we calculate the sum of numbers from 1 to i and store it in the result slice. Finally, we return the result slice.

Please note that the sum of numbers from 1 to i is calculated as i * (i + 1) / 2, which is a mathematical formula for the sum of an arithmetic series. The square of i is calculated as i * i, which is a mathematical formula for the square of a number.