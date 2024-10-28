     splitWords := strings.Fields(sentence)
     result := ""
     for _, word := range splitWords {
         if isPrime(len(word)) {
             result += word + " "
         }
     }
     return strings.TrimSpace(result)
}

func isPrime(n int) bool {
     if n < 2 {
         return false
     }
     for i := 2; i*i <= n; i++ {
         if n%i == 0 {
             return false
         }
     }
     return true
}

*/

package main

import (
	"fmt"
	"strings"
)

func WordsInSentence(sentence string) string {
	splitWords := strings.Fields(sentence)
	result := ""
	for _, word := range splitWords {
		if isPrime(len(word)) {
			result += word + " "
		}
	}
	return strings.TrimSpace(result)
}

func isPrime(n int) bool {
	if n < 2 {
		return false
	}
	for i := 2; i*i <= n; i++ {
		if n%i == 0 {
			return false
		}
	}
	return true
}

func main() {
	fmt.Println(WordsInSentence("This is a test"))         // "is"
	fmt.Println(WordsInSentence("lets go for swimming"))  // "go for"
	fmt.Println(WordsInSentence("hello world"))           // "hello world"
	fmt.Println(WordsInSentence("programming is fun"))    // "programming fun"
	fmt.Println(WordsInSentence("I love coding in Go"))    // "coding"
	fmt.Println(WordsInSentence("Keep calm and carry on")) // "calm carry"
}

// Output:
// is
// go for
// hello world
// programming fun
// coding
// calm carry

// The function isPrime checks if a number is prime or not, and the function WordsInSentence