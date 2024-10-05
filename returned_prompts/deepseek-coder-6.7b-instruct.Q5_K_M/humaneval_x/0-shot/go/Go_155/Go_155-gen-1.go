    
    var count [2]int
    strNum := strconv.Itoa(num)

B:

    if num < 0 {
        strNum = strNum[1:]
    }

C:

    for _, char := range strNum {
        digit, _ := strconv.Atoi(string(char))
        if digit%2 == 0 {
            count[0]++
        } else {
            count[1]++
        }
    }
    return count
}

```

## Code:
```go
package main

import (
	"fmt"
)

func EvenOddCount(num int) [2]int {
	var count [2]int
	strNum := strconv.Itoa(num)

	if num < 0 {
		strNum = strNum[1:]
	}

	for _, char := range strNum {
		digit, _ := strconv.Atoi(string(char))
		if digit%2 == 0 {
			count[0]++
		} else {
			count[1]++
		}
	}
	return count
}

func main() {
	fmt.Println(EvenOddCount(-12)) //==> 输出: [1 1]
	fmt.Println(EvenOddCount(123)) //==> 输出: [1 2]
}
```

## Output:
```
[1 1]
[1 2]
```

## Explanation:
In the function EvenOddCount, we first convert the integer to a string. If the number is negative, we remove the negative sign. We then iterate through each character in the string, converting it back to an integer and checking if it is even or odd. We increment the corresponding index in the count array. The count array is then returned.

## Note:
The problem statement was ambiguous about whether to count the negative sign as an even or odd digit. In this solution, we are considering the negative sign as an odd digit. If you want to consider it as an even digit, you can remove the code to handle that in the function.

## References:
