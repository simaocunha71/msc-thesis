
    // Your code goes here
    return 0
}

// end of code

*/

package main

import (
	"fmt"
)

func GetMaxTriples(n int) int {
	var a = make([]int, n)
	var count = 0
	for i := 1; i <= n; i++ {
		a[i-1] = i*i - i + 1
	}

	for i := 0; i < n; i++ {
		for j := i + 1; j < n; j++ {
			for k := j + 1; k < n; k++ {
				if (a[i]+a[j]+a[k])%3 == 0 {
					count++
				}
			}
		}
	}
	return count
}

func main() {
	fmt.Println(GetMaxTriples(5))
}

//end of code
package main

import (
	"fmt"
)

// Function to calculate the max triples
func GetMaxTriples(n int) int {
	var a = make([]int, n)
	var count = 0
	for i := 1; i <= n; i++ {
		a[i-1] = i*i - i + 1
	}

	for i := 0; i < n; i++ {
		for j := i + 1; j < n; j++ {
			for k := j + 1; k < n; k++ {
				if (a[i]+a[j]+a[k])%3 == 0 {
					count++
				}
			}
		}
	}
	return count
}

// Driver function
func main() {
	fmt.Println(GetMaxTriples(5))
}

// end of code
package main

import (
	"fmt"
)

func main() {
	arr := []int{1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
	target := 5

	result := binarySearch(arr, target)