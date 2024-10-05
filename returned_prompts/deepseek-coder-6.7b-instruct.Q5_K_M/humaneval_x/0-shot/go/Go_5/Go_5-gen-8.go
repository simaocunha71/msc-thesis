
    var result []int

    for i, num := range numbers {
        result = append(result, num)
        if i != len(numbers)-1 {
            result = append(result, delimeter)
        }
    }

    return result
}

*/

package main

import (
	"fmt"
)

func Intersperse(numbers []int, delimeter int) []int {
	var result []int

	for i, num := range numbers {
		result = append(result, num)
		if i != len(numbers)-1 {
			result = append(result, delimeter)
		}
	}

	return result
}

func main() {
	fmt.Println(Intersperse([]int{}, 4))
	fmt.Println(Intersperse([]int{1, 2, 3}, 4))
}

/*
Possible output:
[]
[1 4 2 4 3]
*/

/*
Time complexity:
O(n) because it's a single loop that traverses the slice once.

Space complexity:
O(n) because it creates a new slice that could potentially be the same size as the input.
*/
package main

import (
	"fmt"
	"math"
)

func isPrime(n int) bool {
	if n <= 1 {
		return false
	}

	if n == 2 {
		return true
	}

	if n%2 == 0 {
		return false
	}

	sqrtN := int(math.Sqrt(float64(n)))
	for i := 3; i <= sqrtN; i += 2 {
		if n%i == 0 {
			return false
		}
	}

	return true
}

func main() {
	num := 17
	fmt.Printf("Is %d a prime number? %t\n", num, isPrime(num))
}

/*
Possible output:
Is 17 a prime number? true
*/

/*
Time complexity:
O(sqrt(n)) because in the