
    if strings.Contains(txt, " ") {
        return strings.Split(txt, " ")
    } else if strings.Contains(txt, ",") {
        return strings.Split(txt, ",")
    } else {
        count := 0
        for _, c := range txt {
            if 'a' <= c && c <= 'z' && int(c-'a')%2 == 1 {
                count++
            }
        }
        return count
    }

}

*/

package main

import (
	"fmt"
	"strings"
)

// Given a string of words, return a list of words split on whitespace, if no whitespaces exists in the text you
// should split on commas ',' if no commas exists you should return the number of lower-case letters with odd order in the
// alphabet, ord('a') ≡ 0, ord('b') ≡ 1, … ord('z') ≡ 25
// Examples
// SplitWords("Hello world✔") ➞ ✔["Hello", "world✔"]
// SplitWords("Hello,world✔") ➞ ✔["Hello", "world✔"]
// SplitWords("abcdef") ➞ 3
func SplitWords(txt string) interface{} {

	if strings.Contains(txt, " ") {
		return strings.Split(txt, " ")
	} else if strings.Contains(txt, ",") {
		return strings.Split(txt, ",")
	} else {
		count := 0
		for _, c := range txt {
			if 'a' <= c && c <= 'z' && int(c-'a')%2 == 1 {
				count++
			}
		}
		return count
	}

}

func main() {
	fmt.Println(SplitWords("Hello world!"))  // ➞ ["Hello", "world!"]
	fmt.Println(SplitWords("Hello,world!"))  // ➞ ["Hello", "world!"]
	f