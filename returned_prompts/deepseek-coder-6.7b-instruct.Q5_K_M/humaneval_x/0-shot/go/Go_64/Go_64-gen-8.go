    vowels := []string{"a", "e", "i", "o", "u"}
    count := 0

B:
    s = strings.ToLower(s)

C:
    for _, letter := range s {
        for _, vowel := range vowels {
            if string(letter) == vowel {
                count++
            }
        }
    }

D:
    if len(s) > 0 && s[len(s)-1:] == "y" {
        count++
    }

E:
    return count
}


A: Start by declaring a list of vowels.

B:
Change the input string to lowercase. This step is important because we want the function to be case insensitive.

C:
Iterate over the string. For each letter, check if it is a vowel. If it is, increment the count.

D:
Check if the last letter of the string is 'y'. If it is, increment the count.

E:
Return the count.
*/

package main

import (
	"fmt"
)

func main() {
	fmt.Println(VowelsCount("abcde")) // 2
	fmt.Println(VowelsCount("ACEDY")) // 3
}

func VowelsCount(s string) int {
	vowels := []string{"a", "e", "i", "o", "u"}
	count := 0

	s = strings.ToLower(s)

	for _, letter := range s {
		for _, vowel := range vowels {
			if string(letter) == vowel {
				count++
			}
		}
	}

	if len(s) > 0 && s[len(s)-1:] == "y" {
		count++
	}

	return count
}

/*
Explanation:
The function VowelsCount takes a string s as input. It first converts the string to lowercase. Then it iterates over the string, checking each letter to see if it is a vowel. If it is, it increments the count. If the last letter of the string