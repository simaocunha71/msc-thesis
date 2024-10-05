Here is a Go solution for the problem:

```go
import (
    "math"
    "sort"
)

func NextSmallest(lst []int) interface{} {
    if len(lst) < 2 {
        return nil
    }
    sort.Ints(lst)
    for i := 1; i < len(lst); i++ {
        if lst[i] != lst[0] {
            return lst[i]
        }
    }
    return nil
}
```

This function sorts the list and then checks each element from the second element to the end. If it finds an element that is different from the smallest element, it returns that element. If it doesn't find any such element, it returns nil. 

The time complexity of this function is O(n log n) due to the sorting operation, where n is the length of the list. The space complexity is O(1) as it only uses a constant amount of space. 