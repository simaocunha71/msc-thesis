    result := make([]string, 0)
    v := strings.Fields(s)
    for _, w := range v {
        count := 0
        for _, c := range w {
            if !IsVowel(c) {
                count += 1
            }
        }
        if count == n {
            result = append(result, w)
        }
    }
    return result
}



