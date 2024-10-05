Here is a possible solution:
```go
import (
    "sort"
)

func SortThird(l []int) []int {
    result := make([]int, len(l))
    j := 0
    for i, v := range l {
        if i%3 == 0 {
            // indices that are divisible by three, sort
            sort.Ints(&[]int{v})
            v = []int{v}[0]
        }
        result[j] = v
        j++
    }
    return result
}
```
This function creates a new slice `result` with the same length as the input slice `l`. It then iterates over the input slice, and for each element, it checks if the index is divisible by 3. If it is, it sorts the element and assigns the sorted value to the corresponding index in the `result` slice. If the index is not divisible by 3, it simply assigns the original value to the corresponding index in the `result` slice. Finally, it returns the `result` slice.

Note that this function uses the `sort.Ints` function to sort the element, which is a stable sort, meaning that it preserves the order of equal elements. This is important because the problem statement requires that the values at the indices that are divisible by three are equal to the values of the corresponding indices of `l`, but sorted. If the sort were not stable, the order of equal elements would be lost, and the resulting slice would not be identical to the original slice in the indices that are not divisible by three.