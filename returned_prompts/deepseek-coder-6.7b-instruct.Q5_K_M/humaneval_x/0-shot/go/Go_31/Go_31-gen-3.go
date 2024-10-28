
// Write your code here

}

// Test function
func main() {
    fmt.Println(IsPrime(6))
    fmt.Println(IsPrime(101))
    fmt.Println(IsPrime(11))
    fmt.Println(IsPrime(13441))
    fmt.Println(IsPrime(61))
    fmt.Println(IsPrime(4))
    fmt.Println(IsPrime(1))
}

*/

package main

import (
	"fmt"
	"math"
)

func IsPrime(n int) bool {
	if n <= 1 {
		return false
	}
	if n <= 3 {
		return true
	}
	if n%2 == 0 || n%3 == 0 {
		return false
	}
	i := 5
	for i*i <= n {
		if n%i == 0 || n%(i+2) == 0 {
			return false
		}
		i += 6
	}
	return true
}

func main() {
	fmt.Println(IsPrime(6))
	fmt.Println(IsPrime(101))
	fmt.Println(IsPrime(11))
	fmt.Println(IsPrime(13441))
	fmt.Println(IsPrime(61))
	fmt.Println(IsPrime(4))
	fmt.Println(IsPrime(1))
}
package main

import "fmt"

// 