    for i := 0; i < len(b); i++ {
        for j := 0; j < len(b); j++ {
            var temp = b[j:]
            if i > 0 {
                temp = temp[1:] + temp[0:1]
            }
            if strings.Contains(a, temp) {
                return true
            }
        }
    }
    return false
}