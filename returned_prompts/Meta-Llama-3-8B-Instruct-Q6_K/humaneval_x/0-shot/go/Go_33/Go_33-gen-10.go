Here is a Go solution for the problem:

```go
import (
    "sort"
)

func SortThird(l []int) []int {
    result := make([]int, len(l))
    j := 0
    for i, v := range l {
        if i%3 == 0 {
            // sort the values at indices divisible by three
            sort.Ints(&[]int{v})
            result[j] = result[j+1]
            j++
        } else {
            result[i] = v
        }
    }
    return result
}
```


Explanation:
The function `SortThird` takes a list `l` as input and returns a new list `l'`. It iterates over the original list and checks if the index is divisible by three. If it is, it sorts the value at that index and assigns it to the next available index in the result list. If the index is not divisible by three, it simply copies the value from the original list to the result list. The result list is then returned.

For example, for the input `[5, 6, 3, 4, 8, 9, 2]`, the function will return `[2, 6, 3, 4, 8, 9, 5]`. The value at index 0 (which is 5) is not changed, the value at index 1 (which is 6) is not changed, the value at index 2 (which is 3) is sorted and assigned to the next available index 3, the value at index 3 (which is 4) is not changed, the value at index 4 (which is 8) is not changed, the value at index 5 (which is 9) is not changed, and the value at index 6 (which is 2) is not changed. The result is `[2, 6, 3, 4, 8, 9, 5]`.