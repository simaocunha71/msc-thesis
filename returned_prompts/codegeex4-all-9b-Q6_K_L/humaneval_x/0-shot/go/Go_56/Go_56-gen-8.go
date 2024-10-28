func CorrectBracketing(brackets string) bool {
    open := 0
    for _, c := range brackets {
        switch c {
        case '<':
            open++
        case '>':
            open--
        }
        if open < 0 {
            return false
        }
    }
    return open == 0
}