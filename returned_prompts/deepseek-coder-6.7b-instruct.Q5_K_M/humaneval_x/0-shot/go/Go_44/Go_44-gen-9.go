    if x < base {
        return strconv.Itoa(x)
    }

B:
    _, remainder := divmod(x, base)
    return ChangeBase(x/base, base) + strconv.Itoa(remainder)
}

func divmod(x, base int) (int, int) {
    return x / base, x % base
}

The function divmod is a helper function to divide x by base and return the quotient and the remainder.
The base case is when x < base, in which case the function just converts x into a string using strconv.Itoa.
The recursive case is when x >= base, in which case the function recursively calls itself with x divided by base and concatenates the remainder to the end.
The recursion continues until the base case is reached, and the string representation of the final result is returned.
*/

package main

import (
	"fmt"
)

// Change numerical base of input number x to base.
// return string representation after the conversion.
// base numbers are less than 10.
func ChangeBase(x int, base int) string {
	if x < base {
		return string(x + '0')
	}
	_, remainder := divmod(x, base)
	return ChangeBase(x/base, base) + string(remainder+'0')
}

func divmod(x, base int) (int, int) {
	return x / base, x % base
}

func main() {
	fmt.Println(ChangeBase(8, 3))  // Outputs: 22
	fmt.Println(ChangeBase(8, 2))  // Outputs: 1000
	fmt.Println(ChangeBase(7, 2))  // Outputs: 111
}

/*
This program uses recursion to convert a decimal number to a given base. The base case is when the input number is less than the base, in which case the number is directly converted to a string. The recursive case is when the input number is greater than or equal to the base, in which case the function is called again with the quotient of the input number divided by the base