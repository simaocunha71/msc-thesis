
    // base cases
    if n == 0 || n == 1 {
        return 0
    } else if n == 2 {
        return 2
    } else if n == 3 {
        return 0
    }

B:

    // initialize the first four Fib4 numbers
    a, b, c, d := 0, 0, 2, 0
    var e int

C:

    // iterate to find n-th Fib4 number
    for i := 4; i <= n; i++ {
        e = a + b + c + d
        a, b, c, d = b, c, d, e
    }

    return e
}

D:

    // the n-th Fib4 number is the last calculated number

E:

    // return the n-th Fib4 number
    return e
}

This solution has a time complexity of O(n) because it only requires a single loop to compute the n-th Fib4 number. The space complexity is O(1) because it only requires a constant amount of space to store the first four Fib4 numbers and the n-th Fib4 number.
*/
package main

import "fmt"

func Fib4(n int) int {
	if n == 0 || n == 1 {
		return 0
	} else if n == 2 {
		return 2
	} else if n == 3 {
		return 0
	}

	a, b, c, d := 0, 0, 2, 0
	var e int

	for i := 4; i <= n; i++ {
		e = a + b + c + d
		a, b, c, d = b, c, d, e
	}

	return e
}

func main() {
	fmt.Println(Fib4(5)) // 4
	fmt.Println(Fib4(6)) // 8
	fmt.Println(Fib4(7)) // 14
}

/*
Output:
4
8
14
*/

/*
This program defines a function Fib4(n int) int