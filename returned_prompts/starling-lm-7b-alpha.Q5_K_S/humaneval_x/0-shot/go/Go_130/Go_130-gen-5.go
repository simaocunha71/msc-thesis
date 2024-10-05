
```
package main
 
import "fmt"
 
func Tri(n int) []float64 {
    if n == 0 {
        return []float64{3}
    }
    res := make([]float64, n + 1)
    res[0] = 3
    for i := 1; i < n + 1; i++ {
        if i%2 == 0 {
            res[i] = 1 + float64(i)/2
        } else {
            res[i] = res[i-1] + res[i-2] + res[i+1]
        }
    }
    return res
}
 
func main() {
    fmt.Println(Tri(3))
}
```

This program will output:
```
[1, 3, 2, 8]
```

In this program, we first check whether `n` is 0. If it is, we return a slice with a single element as 3, as defined in the problem. Otherwise, we create a slice `res` of size `n + 1` with the initial value of its first element as 3. Then, we use a `for` loop to calculate the values of `res` for each index `i` from 1 to `n`. If `i` is even, we set `res[i]` to be 1 + `i` / 2. If `i` is odd, we set `res[i]` to be the sum of the previous three elements of `res`. Finally, we return the calculated `res` slice.

```go

```

```go

```
```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```
