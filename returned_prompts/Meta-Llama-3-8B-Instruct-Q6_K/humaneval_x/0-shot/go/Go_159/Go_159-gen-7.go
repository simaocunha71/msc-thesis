```go
package main

import "fmt"

func Eat(number, need, remaining int) []int {
    total := number + need
    if remaining < need {
        total = number + remaining
        return []int{total, 0}
    }
    return []int{total, remaining - need}
}

func main() {
    fmt.Println(Eat(5, 6, 10))  // [11, 4]
    fmt.Println(Eat(4, 8, 9))   // [12, 1]
    fmt.Println(Eat(1, 10, 10)) // [11, 0]
    fmt.Println(Eat(2, 11, 5))  // [7, 0]
}
```


Output:
```go
[11 4]
[12 1]
[11 0]
[7 0]
```


Explanation:
The function `Eat` takes three parameters: `number` (the number of carrots you have eaten), `need` (the number of carrots you need to eat), and `remaining` (the number of remaining carrots). It returns an array of two elements: the total number of carrots eaten after your meals and the number of carrots left after your meals.

In the function, it first calculates the total number of carrots eaten by adding `number` and `need`. If there are not enough remaining carrots to fulfill the need, it sets the total number of carrots eaten to `number` plus the remaining carrots and returns an array with the total number of carrots eaten and 0 as the number of carrots left.

If there are enough remaining carrots to fulfill the need, it sets the total number of carrots eaten to `number` plus `need` and returns an array with the total number of carrots eaten and the remaining carrots minus `need` as the number of carrots left.