    vowels := []string{"a", "e", "i", "o", "u"}
    count := 0
    s = strings.ToLower(s)
    for _, v := range vowels  {
        count += strings.Count(s, v)
    }
    if strings.HasSuffix(s, "y")  {
        count += 1
    }
    return count
}



