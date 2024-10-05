    for i := len(word) - 2; i > 0; i-- {
        if !bytes.ContainsAny([]byte{word[i]}, "aeiouAEIOU") && 
           bytes.ContainsAny([]byte{word[i-1]}, "bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ") && 
           bytes.ContainsAny([]byte{word[i+1]}, "bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ") {
            for j := i + 1; j < len(word); j++ {
                if bytes.ContainsAny([]byte{word[j]}, "aeiouAEIOU") {
                    return string(word[j])
                }
            }
        }
    }
    return ""
}

*/

package main

import (
	"fmt"
)

func GetClosestVowel(word string) string {
	for i := len(word) - 2; i > 0; i-- {
		if !(word[i] == 'a' || word[i] == 'e' || word[i] == 'i' || word[i] == 'o' || word[i] == 'u' ||
			word[i] == 'A' || word[i] == 'E' || word[i] == 'I' || word[i] == 'O' || word[i] == 'U') &&
			(word[i-1] >= 'b' && word[i-1] <= 'z' || word[i-1] >= 'B' && word[i-1] <= 'Z') &&
			(word[i+1] >= 'b' && word[i+1] <= 'z' || word[i+1] >= 'B' && word[i+1] <= 'Z') {
			for j := i + 1; j < len(word); j++ {
				if (word[j] == 'a' || word[j] == 'e' || word[j] == '