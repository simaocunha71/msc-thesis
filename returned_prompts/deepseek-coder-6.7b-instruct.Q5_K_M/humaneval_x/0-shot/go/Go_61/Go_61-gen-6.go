    openBrackets := "("
    countOpen := 0
    countClose := 0

    for _, c := range brackets {
        if strings.ContainsRune(openBrackets, c) {
            countOpen++
        } else {
            countClose++
        }

        if countClose > countOpen {
            return false
        }
    }

    return countOpen == countClose
}

The main idea is to iterate through the brackets string and count the number of opening and closing brackets. If at any point the number of closing brackets exceeds the number of opening brackets, return false since it is not properly bracketed. After iterating through the entire string, return whether the number of opening and closing brackets are equal to ensure every opening bracket has a corresponding closing bracket.

*/
package main

import (
	"fmt"
)

func CorrectBracketing(brackets string) bool {

	openBrackets := "("
	countOpen := 0
	countClose := 0

	for _, c := range brackets {
		if string(c) == openBrackets {
			countOpen++
		} else {
			countClose++
		}

		if countClose > countOpen {
			return false
		}
	}

	return countOpen == countClose
}

func main() {
	fmt.Println(CorrectBracketing("("))         // false
	fmt.Println(CorrectBracketing("()"))        // true
	fmt.Println(CorrectBracketing("(()())"))    // true
	fmt.Println(CorrectBracketing(")(()"))      // false
	fmt.Println(CorrectBracketing("(()()())"))  // true
	fmt.Println(CorrectBracketing("())"))        // false
	fmt.Println(CorrectBracketing("(())"))       // true
	fmt.Println(CorrectBracketing("((())())"))  // true
}
