import (
    "bytes"
)

// You are given a word. Your task is to find the closest vowel that stands between
// two consonants from the right side of the word (case sensitive).
// 
// Vowels in the beginning and ending doesn't count. Return empty string if you didn't
// find any vowel met the above condition.
// 
// You may assume that the given string contains English letter only.
// 
// Example:
// GetClosestVowel("yogurt") ==> "u"
// GetClosestVowel("FULL") ==> "U"
// GetClosestVowel("quick") ==> ""
// GetClosestVowel("ab") ==> ""
func GetClosestVowel(word string) string {
    vowels := []rune("aeiouy")
    
    for len(word) > 0 {
        i, l := 0, len(vowels)
        
        for ; l >= 0 && word[l] == ' '; l--;
        if l < 0 { return "" }
        
        n, l = 1, l + 1
        
        for ; i <= l-1 && (word[i] != 'e' || word[i+n:][len(vowels)-l-1] == 'y'); i++ {
            l -= len(vowels) - n
            
            if l < 0 { return "" }
        }
        
        if i > l && (word[i] != 'e' || word[i+n:][len(vowels)-l-1] == 'y') { 
            return string(vowels[:l]) + "e"
        }
    }
    
    return ""
}

// n is the index of the first letter of the word (excluding case). l is the index of
// last letter of a run (starting from the beginning, excluding the '.' char).
// p is the index of ".".
func get_char(word string, n int) string {
    if n < 0 || len(word) <= n + 1 || word[n:][len(string