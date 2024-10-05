
// Check if two words have the same characters.
// 
// Example:
// 
// SameChars('eabcdzzzz', 'dddzzzzzzzddeddabc') -> true
// SameChars('abcd', 'dddddddabc') -> true
// SameChars('dddddddabc', 'abcd') -> true
// SameChars('eabcd', 'dddddddabc') -> false
// SameChars('abcd', 'dddddddabce') -> false
// SameChars('eabcdzzzz', 'dddzzzzzzzddddabc') -> false
func SameChars(s0 string, s1 string) bool {

// Create character count maps
charCounts0 := make(map[rune]int)
charCounts1 := make(map[rune]int)

// Count characters in each string
for _, char := range s0 {
charCounts0[char]++
}
for _, char := range s1 {
charCounts1[char]++
}

// Check if character counts are equal
if len(charCounts0) != len(charCounts1) {
return false
}
for char, count := range charCounts0 {
if charCounts1[char] !