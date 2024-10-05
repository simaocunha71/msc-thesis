    count := 0
    for _, n := range nums {
        if n > 10 && n%2 != 0 {
            if _, err := strconv.ParseInt(string(rune(n)), 10, 64); err == nil && n%2 != 0 {
                _, _ = strconv.ParseInt(string(rune(n)), 10, 64);
                count++
            }
        }
    }
    return count
}



