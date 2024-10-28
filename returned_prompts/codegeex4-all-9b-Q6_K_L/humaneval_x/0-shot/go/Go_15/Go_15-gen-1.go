func StringSequence(n int) string {
    if n == 0 {
        return "0"
    }
    var sb strings.Builder
    for i := 0; i <= n; i++ {
        sb.WriteString(strconv.Itoa(i))
        if i != n {
            sb.WriteString(" ")
        }
    }
    return sb.String()
}
