    if strings.Contains(txt, " ") || strings.Contains(txt, ",") {
        return strings.Fields(txt)
    }else {
        count := 0
        for _, r := range txt {
            if r >= 'a' && r <= 'z' {
                if r % 2 != 0 {
                    count++
                }
            }
        }
        return count
    }
}



