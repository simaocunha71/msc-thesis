import (
    "strconv"
)

// Given an integer. return a tuple that has the number of even and odd digits respectively.
// 
// Example:
// EvenOddCount(-12) ==> (1, 1)
// EvenOddCount(123) ==> (1, 2)
func EvenOddCount(num int) [2]int {

func EvenOddCount(num int) [2]int {
    var res [2]int
    for i := 0; i < len(strconv.Itoa(num)); i++ {
        digit := strconv.Itoa(num)[i]
        if digit % 2 == 0 {
            res[0]++
        } else {
            res[1]++
        }
    }
    return res
}

func EvenOddCount(num int) [2]int {
    var res [2]int
    for i := 0; i < len(strconv.Itoa(num)); i++ {
        digit := strconv.Itoa(num)[i]
        if digit % 2 == 0 {
            res[0]++
        } else {
            res[1]++
        }
    }
    return res
}

func EvenOddCount(num int) [2]int {
    var res [2]int
    for i := 0; i < len(strconv.Itoa(num)); i++ {
        digit := strconv.Itoa(num)[i]
        if digit % 2 == 0 {
            res[0]++
        } else {
            res[1]++
        }
    }
    return res
}

func EvenOddCount(num int) [2]int {
    var res [2]int
    for i := 0; i < len(strconv.Itoa(num)); i++ {
        digit := strconv.Itoa(num)[i]
        if digit % 2 == 0 {
            res[0]++
        } else {
            res[1]++
        }
    }
    return res
}

func Even