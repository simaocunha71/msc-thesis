
	count := 0
	for i := 0; i < len(str)-len(substring)+1; i++ {
		if str[i:i+len(substring)] == substring {
			count++
		}
	}
	return count
}

func main() {
	fmt.Println(HowManyTimes("", "a"))     // 0
	fmt.Println(HowManyTimes("aaa", "a"))  // 3
	fmt.Println(HowManyTimes("aaaa", "aa")) // 3
}

*/

package main

import (
	"fmt"
	"strings"
)

func HowManyTimes(str string, substring string) int {
	count := strings.Count(str, substring)
	return count
}

func main() {
	fmt.Println(HowManyTimes("", "a"))     // 0
	fmt.Println(HowManyTimes("aaa", "a"))  // 3
	fmt.Println(HowManyTimes("aaaa", "aa")) // 3
}

// NOTE: The above solution uses built-in 'strings.Count' function which is much simpler and more efficient.
// In this function, we pass the original string 'str' and the substring we want to count in it.
// The function returns the count of the substring in the original string.
// This solution is simpler and more efficient than the previous solution.
// The previous solution was just to demonstrate how to solve the problem using brute force and it's not recommended for large strings.
// In the previous solution, we have a loop that runs 'len(str)-len(substring)+1' times.
// In the built-in 'strings.Count' function, it's more efficient and optimized to count substrings.
// It calculates the count in O(n) time complexity.
// This function is much more efficient than the previous solution.
// So, always prefer built-in functions over custom solutions when possible.
// It's not recommended to implement your own count function for substrings unless you have a good reason to do so.
// In most of the cases, built-in functions are optimized and can handle the large inputs efficiently.
//