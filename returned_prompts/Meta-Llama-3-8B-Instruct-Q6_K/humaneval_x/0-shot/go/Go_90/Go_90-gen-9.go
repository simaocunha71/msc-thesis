Here is a Go function that meets the requirements:
```go
import (
    "math"
    "sort"
)

func NextSmallest(lst []int) interface{} {
    sort.Ints(lst)
    if len(lst) < 2 {
        return nil
    }
    for i := 1; i < len(lst); i++ {
        if lst[i] > lst[0] {
            return lst[i]
        }
    }
    return nil
}
```
Here's an explanation of the code:

1. We sort the input list using the `sort.Ints` function.
2. If the length of the list is less than 2, we return `nil` since there is no 2nd smallest element.
3. We iterate through the list starting from the second element (index 1). For each element, we check if it's greater than the smallest element (which is at index 0). If we find such an element, we return it.
4. If we reach the end of the list without finding a larger element, it means the smallest element is the only element in the list, so we return `nil`.

You can test this function with the examples you provided:
```go
fmt.Println(NextSmallest([]int{1, 2, 3, 4, 5})) // Output: 2
fmt.Println(NextSmallest([]int{5, 1, 4, 3, 2})) // Output: 2
fmt.Println(NextSmallest([]int{})) // Output: nil
fmt.Println(NextSmallest([]int{1, 1})) // Output: nil
``` A: Here is a Go function that meets the requirements:
```go
import (
    "math"
    "sort"
)

func NextSmallest(lst []int) interface{} {
    sort.Ints(lst)
    if len(lst) < 2 {
        return nil
    }
    for i := 1; i < len(lst); i++ {
        if lst[i] > lst[0] {
            return lst[i]
        }
    }
    return nil
}
```
Here's an explanation of the code:

1. We sort the input list using the `sort.Ints` function.
2. If the length of the list is less than 2, we return `nil` since there is no 2nd smallest element.
3. We iterate through the list starting from the second element (index 1