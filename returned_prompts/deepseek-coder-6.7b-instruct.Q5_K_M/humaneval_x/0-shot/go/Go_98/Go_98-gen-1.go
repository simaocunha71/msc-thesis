    count := 0
    for i := 0; i < len(s); i++ {
        if i%2 == 0 {
            switch s[i] {
            case 'A', 'E', 'I', 'O', 'U':
                count++
