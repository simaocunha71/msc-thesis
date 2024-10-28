    str = strings.ToLower(str)
    counter := make(map[rune]int)

    for _, letter := range str {
        counter[letter]++
    }

    return len(counter)
}

This code works by first converting the string to lower case to ensure the comparison is case insensitive. It then creates a map where the keys are the characters in the string and the values are the counts of those characters. The function then returns the length of this map, which is the number of distinct characters in the string.

*/

import (
	"fmt"
	"strings"
)

func CountDistinctCharacters(str string) int {
	str = strings.ToLower(str)
	counter := make(map[rune]int)

	for _, letter := range str {
		counter[letter]++
	}

	return len(counter)
}

func main() {
	fmt.Println(CountDistinctCharacters("xyzXYZ"))
	fmt.Println(CountDistinctCharacters("Jerry"))
}

/*
This program will output:
3
4
*/

/*
Explanation:

In the first example, the string 'xyzXYZ' consists of three distinct characters: 'x', 'y', and 'z'.

In the second example, the string 'Jerry' consists of four distinct characters: 'j', 'e', 'r', and 'y'.

*/
package main

import (
	"fmt"
	"strings"
)

/*
