package main

import "fmt"

func Eat(number, need, remaining int) []int {
    if number+need <= remaining {
        return []int{number + need, remaining - need}
    } else {
        return []int{number + remaining, 0}
    }
}

func main() {
    fmt.Println(Eat(5, 6, 10)) // [11, 4]
    fmt.Println(Eat(4, 8, 9)) // [12, 1]
    fmt.Println(Eat(1, 10, 10)) // [11, 0]
    fmt.Println(Eat(2, 11, 5)) // [7, 0]
}