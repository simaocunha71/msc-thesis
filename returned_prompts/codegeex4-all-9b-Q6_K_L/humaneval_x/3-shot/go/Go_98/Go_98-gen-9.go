    count := 0
    for i:=0; i<len(s); i++{
        c := s[i]
        if i%2 == 0 && strings.ContainsRune("AEIOU", c) {
            count += 1
        }
    }
    return count
}



