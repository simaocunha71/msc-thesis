    var ans []int

    for _, num := range x {
        if hasEvenDigit(num) {
            continue
        }
        ans = append(ans, num)
    }

    sort.Ints(ans)
    return ans
}

func hasEvenDigit(num int) bool {
    for num > 0 {
        if (num%10)%2 == 0 {
            return true
        }
        num /= 10
    }
    return false
}
```

## Test Cases

```go
package main

import (
    "fmt"
    "reflect"
)

func main() {
    fmt.Println(reflect.DeepEqual(UniqueDigits([]int{15, 33, 1422, 1}), []int{1, 15, 33}))  // should print true
    fmt.Println(reflect.DeepEqual(UniqueDigits([]int{152, 323, 1422, 10}), []int{}))  // should print true
    fmt.Println(reflect.DeepEqual(UniqueDigits([]int{111, 222, 333, 444}), []int{111, 333}))  // should print true
}
```

## Explanation

The `hasEvenDigit` function is used to check if a number has an even digit. It does this by getting the remainder of the number when divided by 10 (this gives the last digit of the number), and then checking if that remainder is even.

The `UniqueDigits` function loops over the input list of numbers, and for each number, it checks if it has an even digit using the `hasEvenDigit` function. If the number has an even digit, it skips to the next number in the list. If the number does not have an even digit, it is added to the `ans` list.

Finally, the `ans` list is sorted in increasing order using the `sort.Ints` function, and the sorted list is returned.

The test cases check that the function works correctly by comparing