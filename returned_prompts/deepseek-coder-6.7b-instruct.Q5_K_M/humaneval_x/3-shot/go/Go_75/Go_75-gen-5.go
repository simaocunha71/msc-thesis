    count := 0
    if a < 2 {
        return false
    }
    for i := 2; a != 1; i++ {
        if a%i == 0 {
            count++
            a /= i
            if count > 1 && i%2 == 0 || count > 2 {
                return false
            }
            i--
        }
    }
    return count == 3
}



