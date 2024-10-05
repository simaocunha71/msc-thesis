    if x < base {
        return strconv.Itoa(x)
    } else {
        return ChangeBase(x/base, base) + strconv.Itoa(x%base)
    }
}

In this code, we first check if the input number x is less than the base. If yes, we return x as a string. If not, we recursively call the function on the quotient of x and the base, appended with the remainder of x divided by the base.

This works because it recursively breaks down the number into its constituent digits in the target base.

It will keep breaking down the number until it is less than the base, at which point it will return the digits as a string. The order of the digits will be reversed because of the recursive call stack.
*/

import (
	"strconv"
	"fmt"
)

func ChangeBase(x int, base int) string {
	if x < base {
		return strconv.Itoa(x)
	} else {
		return ChangeBase(x/base, base) + strconv.Itoa(x%base)
	}
}

func main() {
	fmt.Println(ChangeBase(8, 3))  // 22
	fmt.Println(ChangeBase(8, 2))  // 1000
	fmt.Println(ChangeBase(7, 2))  // 111
}

/*
Output:
22
1000
111
*/

/*
This function is useful in programming where you might need to convert numbers from one base to another. For example, in computer science, it is often used to convert binary numbers to decimal or hexadecimal.
*/










































































































