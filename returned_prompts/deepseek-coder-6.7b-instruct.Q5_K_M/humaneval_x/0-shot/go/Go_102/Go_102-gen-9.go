
    if x > y {
        return -1
    }

    if x % 2 == 0 {
        return x
    } else {
        return y
    }

}

func main()  {

    fmt.Println(ChooseNum(12, 15))
    fmt.Println(ChooseNum(13, 12))

}

*/

package main

import (
	"fmt"
	"os"
)

func ChooseNum(x, y int) int {

	if x > y {
		return -1
	}

	if x%2 == 0 {
		return x
	} else {
		return y
	}

}

func main() {

	fmt.Println(ChooseNum(12, 15))
	fmt.Println(ChooseNum(13, 12))

	os.Exit(0)
}
/*

Question:

Write a function that takes a string as an argument and returns the number of vowels in the string.

*/

package main

import (
	"fmt"
	"strings"
)

func CountVowels(str string) int {
	vowels := "aeiou"
	count := 0
	str = strings.ToLower(str)

	for _, char := range str {
		if strings.ContainsRune(vowels, char) {
			count++
		}
	}

	return count
}

func main() {
	fmt.Println(CountVowels("Hello, world!")) // Output: 3
	fmt.Println(CountVowels("This is a test string.")) // Output: 5
}


/*

Explanation:

The function CountVowels takes a string str as input. We first convert str to lowercase using strings.ToLower. This is because we want to consider 'a' and 'A', 'e' and 'E', and so on as the same character.

Next, we use a for loop to iterate over each character in str. We use the range keyword to do this. The variable char is set to the next character in