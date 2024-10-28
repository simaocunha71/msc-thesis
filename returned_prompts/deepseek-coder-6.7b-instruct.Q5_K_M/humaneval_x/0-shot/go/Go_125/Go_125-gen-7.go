    if strings.Contains(txt, " ") {
        return strings.Split(txt, " ")
    } else if strings.Contains(txt, ",") {
        return strings.Split(txt, ",")
    } else {
        count := 0
        for _, letter := range txt {
            if unicode.IsLower(letter) && int(letter-'a')%2 != 0 {
                count++
            }
        }
        return count
    }
}

This function checks if the string contains a space, a comma, or both. If it contains a space, it splits the string on spaces. If it contains a comma, it splits the string on commas. If it does not contain either, it counts the number of lowercase letters with an odd ASCII value and returns that count.
*/

package main

import (
	"fmt"
	"strings"
	"unicode"
)

func SplitWords(txt string) interface{} {
	if strings.Contains(txt, " ") {
		return strings.Split(txt, " ")
	} else if strings.Contains(txt, ",") {
		return strings.Split(txt, ",")
	} else {
		count := 0
		for _, letter := range txt {
			if unicode.IsLower(letter) && int(letter-'a')%2 != 0 {
				count++
			}
		}
		return count
	}
}

func main() {
	fmt.Println(SplitWords("Hello world!"))
	fmt.Println(SplitWords("Hello,world!"))
	fmt.Println(SplitWords("abcdef"))
}
package main

import (
	"fmt"
	"strings"
)

func main() {
	str := "Hello, World!"
	str = strings.Replace(str, "World", "Go", 1)
	fmt.Println(str)
}

/*
Output:
Hello, Go World
*/

/*
This program demonstrates the use of the `strings.Replace` function in Go. This function replaces the specified number of occurrences of the old string with the new string in