
// Your code here

}

*/

package main

import "fmt"

func getMaxTriples(n int) int {
	A := make([]int, n)
	for i := 1; i <= n; i++ {
		A[i-1] = (i * i) - i + 1
	}

	count := 0
	for i := 0; i < n-2; i++ {
		for j := i + 1; j < n-1; j++ {
			for k := j + 1; k < n; k++ {
				if (A[i]+A[j]+A[k])%3 == 0 {
					count++
				}
			}
		}
	}
	return count
}

func main() {
	fmt.Println(getMaxTriples(5)) // Output: 1
	fmt.Println(getMaxTriples(7)) // Output: 6
}
package main

import "fmt"

func main() {
	numbers := []int{1, 2, 3, 4, 5, 6, 7, 8, 9, 10}

	for i, number := range numbers {
		if number%2 == 0 {
			fmt.Println(i, "is even")
		} else {
			fmt.Println(i, "is odd")
		}
	}
}

// This program prints out whether each number in a slice is even or odd.
// It uses a range loop to iterate over the slice. For each iteration,
// it checks if the number is even by using the modulus operator.
// If the remainder of the division by 2 is 0, the number is even. Otherwise, it's odd.
// The index of the number in the slice (i) is also printed along with the result.
// The range loop returns two values on each iteration: the index and the value of the element at that index.
// In this case, we don't actually use the value itself, so we use the blank identifier (_) to ignore it.
// Note: The modulus operator % returns the remainder