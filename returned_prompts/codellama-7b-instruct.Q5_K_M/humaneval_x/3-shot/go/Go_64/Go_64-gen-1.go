    count := 0
    for _, c := range s {
        if strings.Contains("aeiouy", strings.ToLower(string(c))) {
            count += 1
        }
    }
    return count
}



