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
        if lst[i] > lst[0] {
            return lst[i]
        }
    }
    return nil
}
```

This function first checks if the list has less than 2 elements. If so, it returns nil. Then it sorts the list. After sorting, it iterates through the list from the second element to the last. If it finds an element that is greater than the first element, it returns that element. If it doesn't find any such element, it returns nil. 

For example, `NextSmallest([1, 2, 3, 4, 5])` will return 2, `NextSmallest([5, 1, 4, 3, 2])` will return 2, and `NextSmallest([])` will return nil. 

Note that the function returns an interface{} type because the function may return either an int or nil. This is a common pattern in Go when a function can return multiple types. The caller of the function would need to check the type of the returned value to handle these cases correctly.  For example, the caller might do something like this:

```go
result := NextSmallest(lst)
if result == nil {
    // handle the case where the list has less than 2 elements or no 2nd smallest element
} else {
    // handle the case where the function returned an int
}
``` 