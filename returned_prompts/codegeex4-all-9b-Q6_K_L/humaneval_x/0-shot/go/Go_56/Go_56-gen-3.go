func CorrectBracketing(brackets string) bool {
    var stack []string
    for _, b := range brackets {
        if string(b) == "<" {
            stack = append(stack, "<")
        } else {
            if len(stack) == 0 {
                return false
            }
            stack = stack[:len(stack)-1]
        }
    }
    return len(stack) == 0
}