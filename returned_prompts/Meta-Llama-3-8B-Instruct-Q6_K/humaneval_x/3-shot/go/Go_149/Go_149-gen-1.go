    // Filter out strings with odd lengths
    filtered := make([]string, 0)
    for _, str := range lst {
        if len(str) % 2 == 0 {
            filtered = append(filtered, str)
        }
    }

    // Sort by length and then alphabetically
    sort.Slice(filtered, func(i, j int) bool {
        if len(filtered[i]) == len(filtered[j]) {
            return filtered[i] < filtered[j]
        }
        return len(filtered[i]) < len(filtered[j])
    })

    return filtered
}