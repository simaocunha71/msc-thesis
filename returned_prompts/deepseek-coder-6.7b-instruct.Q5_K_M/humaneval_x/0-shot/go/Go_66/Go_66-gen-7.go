
	sum := 0
	
	for _, v := range x {
		if unicode.IsUpper(v) {
			sum += int(v)
		}
	}
	
	return sum
	
}

// Digitsum("") 
// Digitsum("abAB") 
// Digitsum("abcCd") 
// Digitsum("helloE") 
// Digitsum("woArBld") 
// Digitsum("aAaaaXa") 
func main() {

	
	fmt.Println(Digitsum("")) // 0
	fmt.Println(Digitsum("abAB")) // 131
	fmt.Println(Digitsum("abcCd")) // 67
	fmt.Println(Digitsum("helloE")) // 69
	fmt.Println(Digitsum("woArBld")) // 131
	fmt.Println(Digitsum("aAaaaXa")) // 153
}


```




```go

// Code:

package main

import (
	"fmt"
	"unicode"
)

func Digitsum(x string) int {

	sum := 0
	
	for _, v := range x {
		if unicode.IsUpper(v) {
			sum += int(v)
		}
	}
	
	return sum
	
}

func main() {

	fmt.Println(Digitsum("")) // 0
	fmt.Println(Digitsum("abAB")) // 131
	fmt.Println(Digitsum("abcCd")) // 67
	fmt.Println(Digitsum("helloE")) // 69
	fmt.Println(Digitsum("woArBld")) // 131
	fmt.Println(Digitsum("aAaaaXa")) // 153
}

```


```go

// Output:

// 0
// 131
// 67
// 69
// 131
//