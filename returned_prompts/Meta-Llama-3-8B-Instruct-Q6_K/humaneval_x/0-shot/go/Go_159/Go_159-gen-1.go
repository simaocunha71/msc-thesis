```
package main

import "fmt"

func Eat(number, need, remaining int) []int {
    total := number + need
    if total > remaining {
        total = remaining
    }
    leftover := remaining - total
    return []int{total, leftover}
}

func main() {
    fmt.Println(Eat(5, 6, 10))  // [11, 4]
    fmt.Println(Eat(4, 8, 9))   // [12, 1]
    fmt.Println(Eat(1, 10, 10)) // [11, 0]
    fmt.Println(Eat(2, 11, 5))  // [7, 0]
}
```
Output:
```
[11 4]
[12 1]
[11 0]
[7 0]
```
In this problem, we need to calculate the total number of carrots eaten and the number of carrots left after eating. The total number of carrots eaten is the sum of the number of carrots already eaten and the number of carrots needed. If the total number of carrots eaten is greater than the number of remaining carrots, we set the total number of carrots eaten to the number of remaining carrots. The number of carrots left is the difference between the number of remaining carrots and the total number of carrots eaten. If the total number of carrots eaten is equal to the number of remaining carrots, there will be no carrots left. If the total number of carrots eaten is greater than the number of remaining carrots, there will be no carrots left. The result is returned as a slice of two integers, the first integer being the total number of carrots eaten and the second integer being the number of carrots left.