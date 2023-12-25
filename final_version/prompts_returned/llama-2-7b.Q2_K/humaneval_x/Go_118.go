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
    vowels := []rune("a", "e", "i", "o", "u")
    closestVowels := make(map[string]int, len(vowels))
    
    for _, character := range word {
        if strings.ContainsAny(string(character), vowels) {
            if closestVowels[character] == 0 {
                closestVowels[character] = 1
            } else {
                closestVowels[character]++
            }
            
            for _, c := range character {
                if strings.ContainsAny(string(c), vowels) {
                    closestVowels[string(c)] += 1
                }
            }
        } else {
            continue
        }
    }
    
    if len(closestVowels) == 0 || (len(closestVowels) > 1 && strings.ContainsAny("", closestVowels)) {
        return ""
    }
    
    v := ""
    for _, c := range word {
        if !strings.ContainsAny("", closestVowels)[c] {
            continue
        }
        
        v += string(c) + " "
    }
    
    return strings.TrimRightFunc(v[1:])
}