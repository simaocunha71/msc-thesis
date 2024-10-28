    var s string

    for i := 0; i <= n; i++ {
        s += strconv.Itoa(i) + " "
    }

    return s[:len(s)-1]
}

func main() {
    fmt.Println(StringSequence(5))
}
*/

package main

import (
	"fmt"
	"strconv"
)

func StringSequence(n int) string {
	var s string

	for i := 0; i <= n; i++ {
		s += strconv.Itoa(i) + " "
	}

	return s[:len(s)-1]
}

func main() {
	fmt.Println(StringSequence(5))
}

// Output:
// 0 1 2 3 4 5

/*
The function StringSequence(n int) takes an integer as an argument and returns a string of space-delimited numbers from 0 through n inclusive.

The for loop runs from 0 to n (inclusive), converts each integer i to a string using strconv.Itoa, adds a space after the number, and concatenates this to the end of the string s. 

The strconv.Itoa function converts an integer to a string.

Finally, the function returns s with the last character removed (which is always a space).

The main function calls the StringSequence function with the argument 5 and prints the result.
*/
/*
Write a Go program that takes a string as input and returns the number of vowels in the string.

Here's an example:

Input: "Hello, World!"
Output: 3

*/

package main

import (
	"fmt"
	"strings"
)

func countVowels(str string) int {
	vowels := []rune{'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'}
	count := 0
	for _, char := range str {
		if strings.ContainsRune(string(vowels), char) {
			count++
		}
	}
	return count
