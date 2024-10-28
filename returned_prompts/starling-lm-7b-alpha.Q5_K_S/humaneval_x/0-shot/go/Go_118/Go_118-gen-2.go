    vowels := []rune{'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'}
    index := -1
    for i, r := range word {
        if !isConsonant(r) {
            if index == -1 {
                index = i
            }
        } else {
            if index != -1 {
                for _, v := range vowels {
                    if v == r {
                        return string(r)
                    }
                }
                index = -1
            }
        }
    }
    return ""
}

func isConsonant(r rune) bool {
    if r < 'a' || r > 'z' {
        return false
    }
    return !contains(r, []rune{'a', 'e', 'i', 'o', 'u'})
}

func contains(r rune, arr []rune) bool {
    for _, v := range arr {
        if v == r {
            return true
        }
    }
    return false
}

// Time complexity: O(n), space: O(1)
//
// getClosestVowel("yogurt") -> "u"
// getClosestVowel("FULL") -> "U"
// getClosestVowel("quick") -> ""
// getClosestVowel("ab") -> ""

*/
import (
    "bytes"
)

func GetClosestVowel(word string) string {
    vowels := []rune{'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'}
    var left, right int
    for i := 0; i < len(word); i++ {
        if !isConsonant(word[i]) {
            if left == -1 {
                left = i
            }
        } else {
            if left != -1 {
                for _, v := range vowels {
                    if v == word[i] {
                        return string(