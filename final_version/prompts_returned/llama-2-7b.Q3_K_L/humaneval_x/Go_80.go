
// You are given a string s.
// Your task is to check if the string is happy or not.
// A string is happy if its length is at least 3 and every 3 consecutive letters are distinct
// For example:
// IsHappy(a) => false
// IsHappy(aa) => false
// IsHappy(abcd) => true
// IsHappy(aabb) => false
// IsHappy(adb) => true
// IsHappy(xyy) => false
func IsHappy(s string) bool {
    if len(s) < 3 {
        return false
    }
    count := make(map[rune]int, 26)
    for i := range s {
        letter := rune(s[i])
        if _, ok := count[letter]; !ok {
            count[letter] = 1
        } else {
            count[letter]++
        }
    }
    
    // If the sum of every character's count is at most two, then return false
    for letter, count := range count {
        if count <= 2 {
            return false
        }
    }
    // Return true when it has three or more unique letters
    return len(count) > 2
}