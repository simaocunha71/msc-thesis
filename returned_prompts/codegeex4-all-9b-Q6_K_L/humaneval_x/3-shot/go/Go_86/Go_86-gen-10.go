    words := strings.Split(s," ")
    var result string
    for _,w := range words{
        sorted := []rune(w)
        sort.Slice(sorted, func(i, j int) bool {
            return sorted[i] < sorted[j]
        })
        result += string(sorted)
        result += " "
    }
    return strings.TrimSpace(result)
}



