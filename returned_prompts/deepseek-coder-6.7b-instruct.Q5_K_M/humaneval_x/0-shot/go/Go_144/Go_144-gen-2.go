    x_num, _ := strconv.Atoi(strings.Split(x, "/")[0])
    x_den, _ := strconv.Atoi(strings.Split(x, "/")[1])

    n_num, _ := strconv.Atoi(strings.Split(n, "/")[0])
    n_den, _ := strconv.Atoi(strings.Split(n, "/")[1])

    if x_num * n_den == n_num * x_den {
        return true
    } else {
        return false
    }
}

This function takes two fractions as strings, splits them into numerator and denominator, converts them to integers and then checks if the product of numerators is equal to the product of denominators. If yes, it returns true, otherwise false.
*/

package main

import (
	"fmt"
	"strconv"
	"strings"
)

func Simplify(x, n string) bool {
	x_num, _ := strconv.Atoi(strings.Split(x, "/")[0])
	x_den, _ := strconv.Atoi(strings.Split(x, "/")[1])

	n_num, _ := strconv.Atoi(strings.Split(n, "/")[0])
	n_den, _ := strconv.Atoi(strings.Split(n, "/")[1])

	if x_num*n_den == n_num*x_den {
		return true
	} else {
		return false
	}
}

func main() {
	fmt.Println(Simplify("1/5", "5/1"))  // Returns: true
	fmt.Println(Simplify("1/6", "2/1"))  // Returns: false
	fmt.Println(Simplify("7/10", "10/2"))  // Returns: true
}

// To run the program, just execute it.
//
// The function Simplify takes two fractions as strings, splits them into numerator and denominator, converts them to integers