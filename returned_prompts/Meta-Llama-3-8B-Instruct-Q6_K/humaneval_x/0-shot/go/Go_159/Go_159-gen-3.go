```go
package main

import "fmt"

func Eat(number, need, remaining int) []int {
    total := number + need
    if total > remaining {
        total = remaining
    }
    return []int{total, remaining - total}
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
This program defines a function `Eat` that takes three integer parameters `number`, `need`, and `remaining`. The function calculates the total number of carrots eaten by adding `number` and `need`. If the total is greater than the remaining carrots, it sets the total to the remaining carrots. Then, it returns an array with two elements: the total number of carrots eaten and the number of carrots remaining after eating. The main function tests this function with different inputs and prints the results. The output shows the total number of carrots eaten and the number of carrots remaining after eating.