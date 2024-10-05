
func CycpatternCheck(a, b string) bool {
    if b == "" {
        return false
    }
    if len(b) > len(a) {
        return false
    }
    for i := 0; i < len(a); i++ {
        if a[i] == b[0] {
            if isSubstring(a, b) {
                return true
            }
        }
        i = i + len(b)
        if i >= len(a) {
            i = i - len(a)
        }
    }
    return false
}

func isSubstring(a, b string) bool {
    for i := 0; i < len(b); i++ {
        if a[i] != b[i] {
            return false
        }
    }
    return true
}

// Time complexity: O(n)
// Space complexity: O(1)

// You can optimize the above solution by using KMP algorithm to check if the pattern is a substring of text.
// However, since we need to check if the pattern is a substring of text with any rotation, we can't use KMP algorithm directly.
// Here is a modified KMP algorithm to solve the problem:
func CycpatternCheck(a, b string) bool {
    if b == "" {
        return false
    }
    if len(b) > len(a) {
        return false
    }
    next := make([]int, len(b))
    j := 0
    for i := 1; i < len(b); i++ {
        for j != 0 && b[i] != b[j] {
            j = next[j]
        }
        if b[i] == b[j] {
            j++
        }
        next[i] = j
    }
    j = 0
    for i := 0; i < len(a); i++ {
        for j != 0 && b[j] != a[i] {
            j = next[j]
        }
        if b[j] == a[i] {
            j++
        }
       