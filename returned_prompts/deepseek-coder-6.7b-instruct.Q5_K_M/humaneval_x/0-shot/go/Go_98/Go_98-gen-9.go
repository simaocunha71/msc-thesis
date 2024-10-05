The function CountUpper takes a string s as input and counts the number of uppercase vowels at even indices of the string.

B:
The function starts by initializing a variable count to 0 and a string upper to hold all uppercase letters. Then it iterates over the string s with a step of 2 (even indices). For each character at an even index, it checks whether the character is an uppercase vowel (i.e., whether the character is in the string upper). If it is, it increments the count.

Finally, the function returns the count.
*/

package main

import (
	"fmt"
)

func main() {
	fmt.Println(CountUpper("aBCdEf")) // returns 1
	fmt.Println(CountUpper("abcdefg")) // returns 0
	fmt.Println(CountUpper("dBBE")) // returns 0
}

func CountUpper(s string) int {
	count := 0
	upper := "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
	for i:=0; i<len(s); i+=2 {
		if strings.ContainsRune(upper, rune(s[i])) {
			count++
		}
	}
	return count
}
