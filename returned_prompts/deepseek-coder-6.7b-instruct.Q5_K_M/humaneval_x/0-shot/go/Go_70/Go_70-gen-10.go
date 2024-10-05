    sort.Ints(lst)

    result := make([]int, len(lst))

    for i := 0; i < len(lst)/2; i++ {
        result[i*2] = lst[i]
        result[i*2+1] = lst[len(lst)-i-1]
    }

    if len(lst)%2 != 0 {
        result[len(lst)-1] = lst[len(lst)/2]
    }

    return result
}

```


## Test Cases:
```go
package main

import (
	"fmt"
	"reflect"
)

func main() {
	fmt.Println(reflect.DeepEqual(StrangeSortList([]int{1, 2, 3, 4}), []int{1, 4, 2, 3}))
	fmt.Println(reflect.DeepEqual(StrangeSortList([]int{5, 5, 5, 5}), []int{5, 5, 5, 5}))
	fmt.Println(reflect.DeepEqual(StrangeSortList([]int{}), []int{}))
	fmt.Println(reflect.DeepEqual(StrangeSortList([]int{1, 2, 3, 4, 5}), []int{1, 5, 2, 4, 3}))
}
```


## Output:
```go
true
true
true
true
```


## Explanation:
The function `StrangeSortList` sorts the input list in ascending order. It then creates a new list of the same length, and fills it with the minimum value from the sorted list, followed by the maximum value, then the next minimum and so on. If the length of the input list is odd, the middle element is set to the middle value in the sorted list.

The test cases check whether the function `StrangeSortList` returns the correct output for various inputs. If the returned output matches the expected output, the test case passes.

## Note:
The sorting algorithm used here is not the most efficient one for large lists. It'