Here is a possible solution in Go:
```go
import (
    "sort"
)

func SortThird(l []int) []int {
    result := make([]int, len(l))
    j := 0
    for i, v := range l {
        if i%3 == 0 {
            indices := make([]int, 0, len(l)/3)
            for k, x := range l {
                if k%3 == 0 {
                    indices = append(indices, x)
                }
            }
            sort.Ints(indices)
            result[j] = indices[len(indices)-1]
            j++
        } else {
            result[j] = v
            j++
        }
    }
    return result
}
```
This function creates a new slice `result` to store the output. It then iterates over the input slice `l`. If the index `i` is divisible by 3, it extracts the values at indices divisible by 3, sorts them, and assigns the last value to the corresponding index in `result`. Otherwise, it simply copies the value to the corresponding index in `result`. Finally, it returns the `result` slice.