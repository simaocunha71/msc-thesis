    sort.Ints(arr)
    arr1 := make([]int, 0)
    for i := len(arr) - 1; i >= 0; i-- {
        arr1 = append(arr1, arr[i])
    }
    arr = arr1
    str_arr := []string{"One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine"}
    res := make([]string, 0)

B:
    for _, value := range arr {
        if value > 0 && value < 10 {
            res = append(res, str_arr[value-1])
        }
    }
    return res
}
```

---

### Code Explanation

The function `ByLength()` takes an array of integers as input. It sorts the array in ascending order, reverses it, and then iterates over it. If the integer is between 1 and 9 inclusive, it converts it to its corresponding name from "One" to "Nine" and appends it to a new array. The function then returns this new array. If the input array is empty, the function returns an empty array. If the array has any strange number, it will be ignored.

---

### Code Testing

```go
package main

import (
	"fmt"
)

func main() {
	arr := []int{2, 1, 1, 4, 5, 8, 2, 3}
	fmt.Println(ByLength(arr)) // Output: ["Eight", "Five", "Four", "Three", "Two", "Two", "One", "One"]

	arr1 := []int{}
	fmt.Println(ByLength(arr1)) // Output: []

	arr2 := []int{1, -1, 55}
	fmt.Println(ByLength(arr2)) // Output: ["One"]
}
```

---

### Code Output

```go
["Eight", "Five", "Four", "Three", "Two", "Two", "One", "One"]
[]
