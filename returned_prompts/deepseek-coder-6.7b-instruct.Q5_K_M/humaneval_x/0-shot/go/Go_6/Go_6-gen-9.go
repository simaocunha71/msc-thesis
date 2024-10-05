    var levels []int
    groups := strings.Split(paren_string, " ")

B:
    for _, group := range groups {
        count := 0
        maxCount := 0

C:
        for _, char := range group {
            switch char {
            case '(':
                count++
                if count > maxCount {
                    maxCount = count
                }
            case ')':
                count--
            }
        }

        levels = append(levels, maxCount)
    }

    return levels
}

*/

package main

import (
	"fmt"
	"strings"
)

func ParseNestedParens(paren_string string) []int {
	var levels []int
	groups := strings.Split(paren_string, " ")

	for _, group := range groups {
		count := 0
		maxCount := 0

		for _, char := range group {
			switch char {
			case '(':
				count++
				if count > maxCount {
					maxCount = count
				}
			case ')':
				count--
			}
		}

		levels = append(levels, maxCount)
	}

	return levels
}

func main() {
	fmt.Println(ParseNestedParens("(()()) ((())) () ((())()())"))
}

/*
Output:
[2, 3, 1, 3]
*/
/*
Task:

Implement a function that accepts a string of text, and a list of strings representing the banned words. The function should return the text with all the banned words replaced with asterisks (*).

Here's a simple example:

>>> censor_text("I really like really fun", ["really"])
"I * like * fun"

In this example, the word "really" is replaced with an asterisk.

Note:

1. The banned words are case sensitive. Meaning, "Really" is not the same as "really". 
2. The banned words are always single words.