func MatchParens(lst []string) string {
    c1 := 0
    c2 := 0
    for _, str := range lst {
        for _, c := range str {
            if c == '(' {
                c1++
            } else {
                c2++
            }
        }
    }
    if c1 == c2 {
        return "Yes"
    } else {
        return "No"
    }
}

