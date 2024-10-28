You can use the following Go code to solve the problem:

```go
import (
    "sort"
)

func SortThird(l []int) []int {
    result := make([]int, len(l))
    j := 0
    for i, v := range l {
        if i%3 == 0 {
            result[i] = v
        } else {
            result[i] = v
        }
    }
    sort.Ints(result[1::3])
    return result
}
```

In this code, we create a new slice `result` with the same length as the input slice `l`. We then iterate over the input slice and copy the values into the `result` slice. If the index `i` is divisible by 3, we copy the value as is. Otherwise, we also copy the value. After that, we sort the elements at the indices that are not divisible by 3. Finally, we return the `result` slice. The `sort.Ints(result[1::3])` function sorts the slice `result[1::3]` which are the elements at the indices that are not divisible by 3. The `1::3` is a slice slice syntax in Go, it means "start at index 1, and end at the end of the slice, and increment by 3". 

This code assumes that the input slice `l` is not empty. If the input slice can be empty, you should add a check for that. 

This code also assumes that the input slice `l` does not contain duplicate values. If the input slice can contain duplicate values, you should consider sorting the elements at the indices that are not divisible by 3 in descending order if you want to preserve the original order of the elements at the indices that are divisible by 3. 

This code also assumes that the input slice `l` does not contain negative numbers. If the input slice can contain negative numbers, you should consider sorting the elements at the indices that are not divisible by 3 in ascending order if you want to preserve the original order of the elements at the indices that are divisible by 3. 

This code also assumes that the input slice `l` does not contain very large numbers. If the input slice can contain very large numbers, you should consider using a more efficient sorting algorithm than the built-in sort function in Go. 

This code also assumes that the input slice `l` does not contain NaN (Not a Number) or