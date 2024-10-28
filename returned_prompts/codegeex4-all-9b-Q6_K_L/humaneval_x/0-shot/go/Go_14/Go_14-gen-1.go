package main

import (
	"fmt"
	"strings"
)

func AllPrefixes(str string) []string {
	prefixes := []string{}

	for i := range str {
		prefixes = append(prefixes, str[:i+1])
	}

	return prefixes
}

func main() {
	fmt.Println(AllPrefixes("abc")) // ['a', 'ab', 'abc']
	fmt.Println(AllPrefixes(strings.Repeat("a", 10))) // ['a', 'aa', 'aaa', 'aaaa', 'aaaaa', 'aaaaaa', 'aaaaaaa', 'aaaaaaaa', 'aaaaaaaaa', 'aaaaaaaaaa']
}