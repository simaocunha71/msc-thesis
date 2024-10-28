    result := make([]rune, 0, len(str))
    for _, c := range str {
        if strings.ToLower(string(c)) == string(c) {
            result = append(result, strings.ToUpper(string(c)))
        } else {
            result = append(result, strings.ToLower(string(c)))
        }
    }
    return string(result)
}  // or you can use strings.Map() function
func FlipCase(str string) string {
    return strings.Map(func(r rune) rune {
        if unicode.IsLower(r) {
            return unicode.ToUpper(r)
        }
        return unicode.ToLower(r)
    }, str)
}  // this is more efficient and cleaner way to solve this problem.  //  //  //  //  //  //  //  //  //  //  //  //  //  //  //  //  //  //  //  //  //  //  //  //  //  //  //  //  //  //  //  //  //  //  //  //  //  //  //  //  //  //  //  //  //  //  //  //  //  //  //  //  //  //  //  //  //  //  //  //  //  //  //  //  //  //  //  //  //  //  //  //  //  //  //  //  //  //  //  //  //  //  //  //  //  //  //  //  //  //  //  //  //  //  //  //  //  //  //  //  //  //  //  //  //  //  //  //  //  //  //  //  //  //  //  //  //  //  //  //  //  //  //  //  //  //  //  //  //  //  //  //  //  //  //  //  //  //  //  //  //  //  //  //  //  //  //  //  //  //  //  //  //  //  //  //  //  //  //  //  //  //  //  //  //  //  //  //  //  //  //  //  //  //  //  //  //  //  //  //  //  //  //  //  //  //