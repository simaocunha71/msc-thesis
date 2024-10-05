
// The main idea is to keep dividing x by n until x becomes 1
// If at any point x becomes less than 1, then return false
// If x becomes 1, then return true

    if x < n {
        return false
    }

    for x%n == 0 {
        x /= n
    }

    return x == 1
}


*/

import (
	"fmt"
	"math"
)

func IsSimplePower(x int, n int) bool {
	if x < n {
		return false
	}
	for x%n == 0 {
		x /= n
	}
	return x == 1
}

func IsSimplePowerV2(x int, n int) bool {
	if x < n {
		return false
	}

	res := math.Log(float64(x)) / math.Log(float64(n))

	return math.Abs(float64(int(res))-res) < 0.000001
}

func main() {
	fmt.Println(IsSimplePower(1, 4))   // true
	fmt.Println(IsSimplePower(2, 2))   // true
	fmt.Println(IsSimplePower(8, 2))   // true
	fmt.Println(IsSimplePower(3, 2))   // false
	fmt.Println(IsSimplePower(3, 1))   // false
	fmt.Println(IsSimplePower(5, 3))   // false
	fmt.Println(IsSimplePowerV2(1, 4)) // true
	fmt.Println(IsSimplePowerV2(2, 2)) // true
	fmt.Println(IsSimplePowerV2(8, 2)) // true
	fmt.Println(IsSimplePowerV2(3, 2)) // false
	fmt.Println(IsSimplePowerV2(3, 1)) // false
	fmt.Println(IsSimplePowerV2(5, 3)) // false
}
package main

import (
	"fmt"
	"math"
)

/*

