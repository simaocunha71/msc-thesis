func MatchParens(lst []string) string {
    var x, y int
    for _, v := range lst[0] {
        if v == '(' {
            x++
        } else {
            y++
        }
    }
    for _, v := range lst[1] {
        if v == '(' {
            x++
        } else {
            y++
        }
    }
    if x > y {
        return "No"
    }
    return "Yes"
}