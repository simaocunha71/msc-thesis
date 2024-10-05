package main

import "fmt"

func CircularShift(x int,shift int) string {
    if shift > len(fmt.Sprintf("%d", x)) {
        return fmt.Sprintf("%d", x)[len(fmt.Sprintf("%d", x))-1:] + fmt.Sprintf("%d", x)[:len(fmt.Sprintf("%d", x))-1]
    }
    return fmt.Sprintf("%d", x)[shift:] + fmt.Sprintf("%d", x)[:shift]
}

func main() {
    fmt.Println(CircularShift(12, 1))
    fmt.Println(CircularShift(12, 2))
}
