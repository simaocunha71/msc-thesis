    if strings.Contains(txt, " ") {
        return strings.Split(txt, " ")
    } else if strings.Contains(txt, ",") {
        return strings.Split(txt, ",")
    } else {
        count := 0
        for _, char := range txt {
            if 'a' <= char && char <= 'z' {
                if int(char-'a')%2 == 1 {
                    count++
                }
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

func SplitWords(txt string) interface{} {
	if strings.Contains(txt, " ") {
		return strings.Split(txt, " ")
	} else if strings.Contains(txt, ",") {
		return strings.Split(txt, ",")
	} else {
		count := 0
		for _, char := range txt {
			if 'a' <= char && char <= 'z' {
				if int(char-'a')%2 == 1 {
					count++
				}
			}
		}
		return count
	}
}

func main() {
	fmt.Println(SplitWords("Hello world!")) // ➞  ["Hello", "world!"]
	fmt.Println(SplitWords("Hello,world!")) // ➞  ["Hello", "world!"]
	fmt.Println(SplitWords("abcdef"))       // ➞ 3
}

















































































































































