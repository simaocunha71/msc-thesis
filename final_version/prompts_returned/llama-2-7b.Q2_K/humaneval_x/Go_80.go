
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
    if len(s) < 3 || s[0:1] == s[1:]... {
        return false
    }

    for c, i := range s {
        if s[i+1] != c {
            return false
        }
    }
    return true
}
