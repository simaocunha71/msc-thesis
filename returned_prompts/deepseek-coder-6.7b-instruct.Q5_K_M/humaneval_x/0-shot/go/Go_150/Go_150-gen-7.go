
    // Checking if the number is prime
    for i := 2; i < n; i++ {
        if n%i == 0 {
            return y
        }
    }
    return x
}

func main() {

B:

    // Testing the function
    fmt.Println(XOrY(7, 34, 12))  // should return 34
    fmt.Println(XOrY(15, 8, 5))  // should return 5
}

*/
package main

import "fmt"

func XOrY(n, x, y int) int {
	for i := 2; i < n; i++ {
		if n%i == 0 {
			return y
		}
	}
	return x
}

func main() {
	fmt.Println(XOrY(7, 34, 12))  // should return 34
	fmt.Println(XOrY(15, 8, 5))   // should return 5
}

/*
This program is a simple function that takes three integer inputs: n, x, and y. It checks if n is a prime number by looping through all numbers from 2 to n-1 and checking if n is divisible by any of these numbers. If n is divisible by any number, it returns y. If n is not divisible by any number, it returns x.
*/
/*
