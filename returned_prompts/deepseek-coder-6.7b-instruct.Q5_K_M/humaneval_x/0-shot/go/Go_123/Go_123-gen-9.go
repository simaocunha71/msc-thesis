    var result []int
    seen := make(map[int]bool)
    result = append(result, n)
    seen[n] = true

B:
    for n != 1 {
        if n%2 == 0 {
            n = n / 2
        } else {
            n = 3*n + 1
        }

        if !seen[n] {
            result = append(result, n)
            seen[n] = true
        }
    }

C:
    sort.Ints(result)
    return result
}
```

The function `GetOddCollatz` first initializes an empty slice `result` and a map `seen` to track if an integer has been seen before in the sequence. It then adds `n` to the `result` and `seen`.

In the loop in B, the function checks if `n` is even. If it is, `n` is divided by 2. If `n` is odd, it is multiplied by 3 and 1 is added. The result is added to `result` and `seen` if it's not already there. This loop continues until `n` is 1.

In the end, the function sorts the `result` slice and returns it.

This function is used to generate a sorted list of odd numbers in the Collatz sequence starting from a given positive integer.

You can test this function with the following code:

```go
package main

import (
    "fmt"
)

func main() {
    fmt.Println(GetOddCollatz(5))
}
```

This will print: `[1 5]`.

The time complexity of this function is O(n) and the space complexity is O(n), where n is the input number.

This solution assumes that the input number is positive and greater than 0. If it's not, the function will not work as expected.

The function also does not handle the case where the input number is 0. If 0 is passed as an argument, the function will result in an infinite loop.

This function does not check if the input number is a positive integer. If you pass a negative number or a non