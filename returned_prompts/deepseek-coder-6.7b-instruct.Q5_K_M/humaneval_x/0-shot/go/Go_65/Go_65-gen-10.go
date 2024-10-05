
    var s = strconv.Itoa(x)
    var shiftDigits = len(s) - shift
    if shiftDigits < 0 {
        s = reverse(s)
    } else {
        s = s[shiftDigits:] + s[:shiftDigits]
    }
    return s
}

func reverse(s string) string {

B:

    runes := []rune(s)
    for i, j := 0, len(runes)-1; i < j; i, j = i+1, j-1 {
        runes[i], runes[j] = runes[j], runes[i]
    }
    return string(runes)
}

*/
package main

import (
	"fmt"
	"strconv"
)

func CircularShift(x int, shift int) string {
	var s = strconv.Itoa(x)
	var shiftDigits = len(s) - shift
	if shiftDigits < 0 {
		s = reverse(s)
	} else {
		s = s[shiftDigits:] + s[:shiftDigits]
	}
	return s
}

func reverse(s string) string {
	runes := []rune(s)
	for i, j := 0, len(runes)-1; i < j; i, j = i+1, j-1 {
		runes[i], runes[j] = runes[j], runes[i]
	}
	return string(runes)
}

func main() {
	fmt.Println(CircularShift(12, 1)) // 21
	fmt.Println(CircularShift(12, 2)) // 12
}
package main

import "fmt"

func main() {
	a := 5
	b := 10

	a, b = b, a

	fmt.Println("a:", a)
	fmt.Println("b:", b)
}

// a: 10
// b: 5

// Go allows for multiple return values.
// It also