    count := 0
    for _, v := range arr {
        if v < 0 {
            v = v * -1
        }
        sum := 0
        for v > 0 {
            digit := v % 10
            sum += digit
            v = v / 10
        }
        if sum > 0 {
            count++
        }
    }
    return count
}

```

## Solution

```go
package main

import (
	"fmt"
	"strconv"
)

func CountNums(arr []int) int {
	count := 0
	for _, v := range arr {
		str := strconv.Itoa(v)
		sum := 0
		for _, ch := range str {
			digit, _ := strconv.Atoi(string(ch))
			if v < 0 && str[0] == '-' {
				digit = digit * -1
			}
			sum += digit
		}
		if sum > 0 {
			count++
		}
	}
	return count
}

func main() {
	fmt.Println(CountNums([]int{-1, 11, -11})) // 1
	fmt.Println(CountNums([]int{1, 1, 2}))      // 3
	fmt.Println(CountNums([]int{}))              // 0
}
```

## Explanation

In the provided code, we have a function `CountNums` which takes in a slice of integers `arr` as an argument and returns the number of elements in the array that have a sum of their digits greater than 0. 

If the number is negative, we convert it to positive by multiplying it by `-1`. We then iterate over each digit in the number, add it to the `sum` variable, and finally check if the `sum` is greater than 0. If it is, we increment the `count`. 

In the end, we return the `count`.

In the `main` function, we test the `CountNums` function with various test cases.
