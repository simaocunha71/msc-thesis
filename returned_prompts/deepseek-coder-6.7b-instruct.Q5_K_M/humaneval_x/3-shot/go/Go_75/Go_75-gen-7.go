    count := 0
    for i := 2; a != 1; i++ {
        for a % i == 0 {
            count++
            a = a / i
            if count > 3 {
                return false
            }
        }
    }
    return count == 3
}



