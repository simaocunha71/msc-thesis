if len(strings) == 0{
    return nil
  }

  longest := strings[0]
  for _, str := range strings {
    if len(str) > len(longest) {
      longest = str
    }
  }
  return longest
}

*/

package main

import (
	"fmt"
)

func Longest(strings []string) interface{} {
	if len(strings) == 0 {
		return nil
	}

	longest := strings[0]
	for _, str := range strings {
		if len(str) > len(longest) {
			longest = str
		}
	}
	return longest
}

func main() {
	fmt.Println(Longest([]string{}))         // nil
	fmt.Println(Longest([]string{"a", "b", "c"})) // 'a'
	fmt.Println(Longest([]string{"a", "bb", "ccc"})) // 'ccc'
}
package main

import (
	"fmt"
)

func Fibonacci(n int) int {
	if n <= 1 {
		return n
	}
	return Fibonacci(n-1) + Fibonacci(n-2)
}

func main() {
	var n int
	fmt.Print("Enter the position of the Fibonacci sequence to get the value at: ")
	fmt.Scan(&n)
	fmt.Printf("The value at position %d in the Fibonacci sequence is %d\n", n, Fibonacci(n))
}

/*
The Fibonacci sequence is a series of numbers in which each number is the sum of the two preceding ones.

- The sequence starts with 0 and 1.
- The sequence goes 0, 1, 1, 2, 3, 5, 8, 13, 21, and so forth.

This program takes a number n as input and prints the nth number in the Fibonacci sequence.

Note: This is a simple implementation and may not be efficient for large inputs due to