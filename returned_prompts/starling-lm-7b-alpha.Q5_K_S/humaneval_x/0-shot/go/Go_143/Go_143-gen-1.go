    var ans string
    for _, s := range strings.Fields(sentence) {
        if isPrime(len(s)) {
            ans += s + " "
        }
    }
    return ans[:len(ans)-1]
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

*/

/*

You are given a string representing a sentence,
the sentence contains some words separated by a space,
and you have to return a string that contains the words from the original sentence,
whose lengths are prime numbers,
the order of the words in the new string should be the same as the original one.

Example 1:
Input: sentence = "This is a test"
Output: "is"

Example 2:
Input: sentence = "lets go for swimming"
Output: "go for"

Constraints:
* 1 <= len(sentence) <= 100
* sentence contains only letters



*/

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

    var ans string
    for _, s := range strings.Fields(sentence) {
        if isPrime(len(s)) {
            ans += s + " "
        }
    }
    return ans[:len