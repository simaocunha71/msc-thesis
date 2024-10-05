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
	fmt.Println(SplitWords("Hello world!"))
	fmt.Println(SplitWords("Hello,world!"))
	fmt.Println(SplitWords("abcdef"))
}
/*
