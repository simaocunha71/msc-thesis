    var sb strings.Builder
    for _, w := range strings.Fields(s) {
        sb.WriteString(antiShuffle(w))
        sb.WriteString(" ")
    }
    return sb.String()
}

func antiShuffle(s string) string {
    var sb strings.Builder
    for _, c := range []rune(s) {
        for i := ' '; i < c; i++ {
            sb.WriteString(string(i))
        }
        sb.WriteString(string(c))
    }
    return sb.String()
}


func antiShuffle(s string) string {
    var sb strings.Builder
    sort.Slice(s, func(i, j int) bool {
        return int(s[i]) < int(s[j])
    })
    return sb.String()
}


func antiShuffle(s string) string {
    var sb strings.Builder
    for _, r := range []rune(s) {
        for i := ' '; i < r; i++ {
            sb.WriteString(string(i))
        }
        sb.WriteString(string(r))
    }
    return sb.String()
}


func antiShuffle(s string) string {
    var sb strings.Builder
    for _, r := range []rune(s) {
        for i := ' '; i < r; i++ {
            sb.WriteString(string(i))
        }
        sb.WriteString(string(r))
    }
    return sb.String()
}


func antiShuffle(s string) string {
    var sb strings.Builder
    for _, r := range []rune(s) {
        for i := ' '; i < r; i++ {
            sb.WriteString(string(i))
        }
        sb.WriteString(string(r))
    }
    return sb.String()
}


func antiShuffle(s string) string {
    var sb strings.Builder
    for _, r := range []rune(s) {
        for i := ' '; i < r; i++ {
           