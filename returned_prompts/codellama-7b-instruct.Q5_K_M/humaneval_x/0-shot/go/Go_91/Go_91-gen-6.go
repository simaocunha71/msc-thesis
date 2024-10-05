    var r *regexp.Regexp = regexp.MustCompile(`(?i)I`)
    var count int
    var words []string = strings.Split(S, " ")
    for _, word := range words {
        if r.MatchString(word) {
            count++
        }
    }
    return count
}

func main() {
    var S string
    if _, err := fmt.Scan(&S); err != nil {
        panic(err)
    }
    fmt.Println(IsBored(S))
}

EOF

pass;
