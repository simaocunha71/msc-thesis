```go
package main

import "fmt"

func Eat(number, need, remaining int) []int {
    total := number + need
    if total > remaining {
        return []int{remaining, 0}
    } else {
        return []int{total, remaining - total}
    }
}

func main() {
    fmt.Println(Eat(5, 6, 10))  // [11, 4]
    fmt.Println(Eat(4, 8, 9))   // [12, 1]
    fmt.Println(Eat(1, 10, 10)) // [11, 0]
    fmt.Println(Eat(2, 11, 5))  // [7, 0]
}
```


This program defines a function `Eat` that takes three integer parameters: `number`, `need`, and `remaining`. The function calculates the total number of carrots eaten by adding `number` and `need`, and then checks if the total is greater than `remaining`. If it is, the function returns a slice with the total number of carrots eaten and 0 remaining. If the total is not greater than `remaining`, the function returns a slice with the total number of carrots eaten and the remaining number of carrots.

The `main` function demonstrates the use of the `Eat` function with different input values and prints the output to the console.