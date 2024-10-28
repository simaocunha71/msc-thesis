    words := strings.Split(s, " ")
    var output []string
    for _, word := range words {
        count := 0
        for _, char := range word {
            if strings.ContainsRune("bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ", char) {
                count++
            }
        }
        if count == n {
            output = append(output, word)
        }
    }
    return output
}

func main() {
    fmt.Println(SelectWords("Mary had a little lamb", 4)) // should print [little]
    fmt.Println(SelectWords("Mary had a little lamb", 3)) // should print [Mary lamb]
    fmt.Println(SelectWords("simple white space", 2)) // should print []
    fmt.Println(SelectWords("Hello world", 4)) // should print [world]
    fmt.Println(SelectWords("Uncle sam", 3)) // should print [Uncle]
}

*/

package main

import (
	"fmt"
	"strings"
)

func SelectWords(s string, n int) []string {
	words := strings.Split(s, " ")
	var output []string
	for _, word := range words {
		count := 0
		for _, char := range word {
			if strings.ContainsRune("bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ", char) {
				count++
			}
		}
		if count == n {
			output = append(output, word)
		}
	}
	return output
}

func main() {
	fmt.Println(SelectWords("Mary had a little lamb", 4)) // should print [little]
	fmt.Println(SelectWords("Mary had a little lamb", 3)) // should print [Mary lamb]
	fmt.Println(SelectWords("simple white space", 2))     // should print []
	fmt.Println(SelectW