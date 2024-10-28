    if text == "" {
        return nil
    }

    hasher := md5.New()
    hasher.Write([]byte(text))

    return fmt.Sprintf("%x", hasher.Sum(nil))
}

The function takes a string as an argument and returns its MD5 hash equivalent string. If the input string is an empty string, it returns nil. The function makes use of the md5 package provided by the Go standard library to compute the MD5 hash.

*/

// Given a string 'text', return its md5 hash equivalent string.
// If 'text' is an empty string, return nil.
//
// >>> StringToMd5('Hello world') == '3e25960a79dbc69b674cd4ec67a72c62'
func StringToMd5(text string) interface{} {
	if text == "" {
		return nil
	}

	hasher := md5.New()
	hasher.Write([]byte(text))

	return fmt.Sprintf("%x", hasher.Sum(nil))
}

func main() {
	fmt.Println(StringToMd5("Hello world"))
}
package main

import (
	"fmt"
	"strings"
)

// Given a string 'text', return the string in reverse order.
// If 'text' is an empty string, return nil.
//
// >>> ReverseString('Hello world') == 'dlrow olleH'
func ReverseString(text string) interface{} {
	if text == "" {
		return nil
	}

	runes := []rune(text)
	for i, j := 0, len(runes)-1; i < j; i, j = i+1, j-1 {
		runes[i], runes[j] = runes[j], runes[i]
	}

	return string(runes)
}

func main() {
	fmt.Println(ReverseString("Hello world"))
}

/*
