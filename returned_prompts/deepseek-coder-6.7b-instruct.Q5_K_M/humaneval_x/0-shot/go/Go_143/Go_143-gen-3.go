    words := strings.Fields(sentence)
    result := ""

B:
    for _, word := range words {
        if isPrime(len(word)) {
            result += word + " "
        }
    }

    return strings.TrimSpace(result)
}

func isPrime(n int) bool {
    if n <= 1 {
        return false
    }

    for i := 2; i*i <= n; i++ {
        if n%i == 0 {
            return false
        }
    }

    return true
}

```

The function `WordsInSentence` receives a string sentence and splits it into words using `strings.Fields(sentence)`. It then iterates over each word and checks if its length is a prime number using the helper function `isPrime()`. If it is, the word is added to the result string. The `strings.TrimSpace(result)` at the end is used to remove the trailing whitespace.

The `isPrime()` function checks if a number is a prime number by iterating from 2 to the square root of the number and checking if the number is divisible by any of these numbers. If it is, the function returns `false`. If it is not, the function returns `true`.

The time complexity of this solution is O(n*m), where n is the number of words in the sentence and m is the average length of the words. The space complexity is O(n), where n is the number of words in the sentence.
*/
package main

import (
	"fmt"
)

func main() {
	fmt.Println(WordsInSentence("This is a test"))         // Output: "is"
	fmt.Println(WordsInSentence("lets go for swimming")) // Output: "go for"
}

func WordsInSentence(sentence string) string {
	words := strings.Fields(sentence)
	result := ""

	for _, word := range words {
		if isPrime(len(word)) {
			result += word + " "
		}
	}

	return strings.Trim