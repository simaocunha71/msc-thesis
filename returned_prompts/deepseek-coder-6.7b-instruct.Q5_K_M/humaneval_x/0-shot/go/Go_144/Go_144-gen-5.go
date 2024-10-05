    // Convert the x and n to integers
    xNum, _ := strconv.Atoi(strings.Split(x, "/")[0])
    xDen, _ := strconv.Atoi(strings.Split(x, "/")[1])
    nNum, _ := strconv.Atoi(strings.Split(n, "/")[0])
    nDen, _ := strconv.Atoi(strings.Split(n, "/")[1])

    // Calculate the new numerator and denominator
    newNum := xNum * nNum
    newDen := xDen * nDen

    // Check if newNum is divisible by newDen
    if newNum % newDen == 0 {
        return true
    } else {
        return false
    }
}

func main() {
    fmt.Println(Simplify("1/5", "5/1")) // Should print: true
    fmt.Println(Simplify("1/6", "2/1")) // Should print: false
    fmt.Println(Simplify("7/10", "10/2")) // Should print: false
}

This code works by converting the string representation of the fractions to integers, calculating the new numerator and denominator by multiplying the numerators and denominators of the original fractions, and then checking if the new numerator is evenly divisible by the new denominator. If it is, it returns true, indicating that the expression x * n simplifies to a whole number. If not, it returns false.
This code has a time complexity of O(1), which is the best possible time complexity for this problem as it only performs a fixed number of operations.
*/

package main

import (
	"fmt"
	"strconv"
	"strings"
)

func Simplify(x, n string) bool {
	xNum, _ := strconv.Atoi(strings.Split(x, "/")[0])
	xDen, _ := strconv.Atoi(strings.Split(x, "/")[1])
	nNum, _ := strconv.Atoi(strings.Split(n, "/")[