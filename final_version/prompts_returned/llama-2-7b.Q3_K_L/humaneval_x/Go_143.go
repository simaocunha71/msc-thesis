import (
    "strings"
)

// You are given a string representing a sentence,
// the sentence contains some words separated by a space,
// and you have to return a string that contains the words from the original sentence,
// whose lengths are prime numbers,
// the order of the words in the new string should be the same as the original one.
// 
// Example 1:
// Input: sentence = "This is a test"
// Output: "is"
// 
// Example 2:
// Input: sentence = "lets go for swimming"
// Output: "go for"
// 
// Constraints:
// * 1 <= len(sentence) <= 100
// * sentence contains only letters
func WordsInSentence(sentence string) string {
    words := strings.Split(sentence, " ")
    
    res:
	for i := range words {
        length := len(words[i])
        
		if (length == 2 && isPrime(length)) || 
           (length > 2 && isPrime(length) && isPrime(int(length/2))){
            continue res
        }
    }
    
    return "none"
}

func isPrime(num int) bool {
	for i := 0; i < len(num)/2+1; i++ {
		if num%i != 0 {
			return true
		}
	}
	return false
}