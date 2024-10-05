    if strings.Contains(txt," ") || strings.Contains(txt,",") {
        return strings.Fields(txt)
    }else {
        count := 0
        for _,char := range txt {
            if char >= 'a' && char <= 'z' {
                if (char - 'a') % 2 == 1 {
                    count += 1
                }
            }
        }
        return count
    }
}



