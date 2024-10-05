    if text == "" {
        return nil
    }

    hasher := md5.New()
    hasher.Write([]byte(text))
    return fmt.Sprintf("%x", hasher.Sum(nil))
}

*/

package main

import (
	"crypto/md5"
	"fmt"
)

// Given a string 'text', return its md5 hash equivalent string.
// If 'text' is an empty string, return nil.
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
/*
