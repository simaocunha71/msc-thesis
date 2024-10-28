func CorrectBracketing(brackets string) bool {
    var opening, closing int
    for _, c := range brackets {
        switch c {
        case '<':
            opening++
        case '>':
            closing++
        }
    }
    return opening == closing
}