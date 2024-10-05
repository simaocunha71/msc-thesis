func MatchParens(lst []string) string {
    var openParen, closeParen int
    for _, v := range lst {
        for _, c := range v {
            if c == '(' {
                openParen++
            } else if c == ')' {
                closeParen++
            }
        }
    }
    if openParen == closeParen {
        return "Yes"
    }
    return "No"
}