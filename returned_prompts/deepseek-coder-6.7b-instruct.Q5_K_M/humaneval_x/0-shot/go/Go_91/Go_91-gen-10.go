    var (
        counter int
        regex = regexp.MustCompile(`\bI[a-z]*`)
    )

B:
    matches := regex.FindAllString