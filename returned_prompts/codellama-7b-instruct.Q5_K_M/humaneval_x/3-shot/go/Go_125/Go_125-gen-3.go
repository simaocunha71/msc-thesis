    if strings.Contains(txt, " ") {
        return strings.Fields(txt)
    }else if strings.Contains(txt, ","){
        return strings.Fields(txt)
    }else{
        count := 0
        for i := 0; i < len(txt); i++ {
            if txt[i] >= 'a' && txt[i] <= 'z' {
                if i%2 != 0 {
                    count++
                }
            }
        }
        return count
    }
}



