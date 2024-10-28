    result := 0
    for i := 1; i < n; i++ {
        if i%11==0 || i%13==0 {
            for _, c := range strconv.Itoa(i) {
                if c == '7' {
                    result += 1
                    break
                }
            }
        }
    }
    return result
}



