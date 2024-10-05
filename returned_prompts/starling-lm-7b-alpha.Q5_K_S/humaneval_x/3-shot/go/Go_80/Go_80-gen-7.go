    if len(s) < 3 {
        return false
    }

    var visited_chars = make(map[rune]bool)
    for i:=0; i<len(s)-2; i++ {
        c1,c2,c3 := s[i], s[i+1], s[i+2]
        if visited_chars[c1] || visited_chars[c2] || visited_chars[c3] {
            return false
        }
        visited_chars[c1] = true
        visited_chars[c2] = true
        visited_chars[c3] = true
    }
    return true
}




