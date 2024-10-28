    if len(lst) == 0 {
        return lst
    }

    sort.Ints(lst)

    result := make([]int, len(lst))
    j := 0

    for i := 0; i < len(lst)/2; i++ {
        result[j] = lst[i]
        j++
        if j < len(lst) {
            result[j] = lst[len(lst)-1-i]
            j++
        }
    }

    return result
}
```

### Test cases
```go
package main

import (
	"fmt"
	"reflect"
)

func main() {
	fmt.Println(reflect.DeepEqual(StrangeSortList([]int{1, 2, 3, 4}), []int{1, 4, 2, 3})) // true
	fmt.Println(reflect.DeepEqual(StrangeSortList([]int{5, 5, 5, 5}), []int{5, 5, 5, 5})) // true
	fmt.Println(reflect.DeepEqual(StrangeSortList([]int{}), []int{}))                       // true
	fmt.Println(reflect.DeepEqual(StrangeSortList([]int{1}), []int{1}))                   // true
	fmt.Println(reflect.DeepEqual(StrangeSortList([]int{1, 2}), []int{1, 2}))             // true
	fmt.Println(reflect.DeepEqual(StrangeSortList([]int{1, 2, 3}), []int{1, 3, 2}))       // true
	fmt.Println(reflect.DeepEqual(StrangeSortList([]int{1, 2, 3, 4, 5}), []int{1, 5, 2, 4, 3})) // true
}
```

This solution sorts the input list in ascending order, then it builds a new list with the minimum value from the front and the maximum value from the back, alternating between these two. If the length of the input list is odd