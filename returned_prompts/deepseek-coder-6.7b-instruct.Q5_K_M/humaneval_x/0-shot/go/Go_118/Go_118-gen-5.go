    for i:=len(word)-1; i>0; i-- {
        for _, v := range "aeiouAEIOU" {
            if word[i] == byte(v) {
                for _, c := range "bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ" {
                    if word[i-1] == byte(c) && word[i+1] == byte(c) {
                        return string(word[i])
                    }
                }
            }
        }
    }
    return ""
}
```

## 2. 使用Go语言的字符串处理

在Go语言中，处理字符串时，我们可以使用内置的字符串处理函数，如`strings`、`bytes`等。

```go
package main

import (
	"fmt"
	"strings"
)

func GetClosestVowel(word string) string {
	vowels := "aeiouAEIOU"
	consonants := "bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ"

	for i := len(word) - 1; i > 0; i-- {
		if strings.ContainsRune(vowels, rune(word[i])) {
			if strings.ContainsRune(consonants, rune(word[i-1])) && strings.ContainsRune(consonants, rune(word[i+1])) {
				return string(word[i])
			}
		}
	}
	return ""
}

func main() {
	fmt.Println(GetClosestVowel("yogurt")) // 输出："u"
	fmt.Println(GetClosestVowel("FULL"))   // 输出："U"
	fmt.Println(GetClosestVowel("quick"))  // 输出：""
	fmt.Println(GetClosestVowel("ab"))     // 输出：""
}
```

