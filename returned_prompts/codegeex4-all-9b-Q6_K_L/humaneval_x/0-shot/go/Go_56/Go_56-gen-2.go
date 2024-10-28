func CorrectBracketing(brackets string) bool {
    var open int
    for _, b := range brackets {
        if b == '<' {
            open++
        } else if open == 0 {
            return false
        } else {
            open--
        }
    }
    return open == 0
}