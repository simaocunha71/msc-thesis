
    var stones []int
    if n % 2 == 0 {
        for i := 0; i < n; i++ {
            stones = append(stones, n+2*i)
        }
    } else {
        for i := 0; i < n; i++ {
            stones = append(stones, n+2*i)
        }
    }
    return stones
}

*/

package main

import (
	"fmt"
)

func MakeAPile(n int) []int {
	var stones []int
	if n%2 == 0 {
		for i := 0; i < n; i++ {
			stones = append(stones, n+2*i)
		}
	} else {
		for i := 0; i < n; i++ {
			stones = append(stones, n+2*i)
		}
	}
	return stones
}

func main() {
	fmt.Println(MakeAPile(3))
	fmt.Println(MakeAPile(4))
	fmt.Println(MakeAPile(5))
}
package main

import "fmt"

// Problem 1:

// Given a string, count the number of vowels in it.

// Example:
// "hello" => 2

func CountVowels(s string) int {
	count := 0
	for _, char := range s {
		switch char {
		case 'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U':
			count++
		}
	}
	return count
}

func main() {
	fmt.Println(CountVowels("hello"))
}

// Problem 2:

// Given a string, count the number of words in it.

// Example:
// "hello world" => 2

func CountWords(s string) int {
	count := 0
	for _, char := range s {
		if char == ' ' {
			count++
		}
	}
	return count + 1
}

func main() {