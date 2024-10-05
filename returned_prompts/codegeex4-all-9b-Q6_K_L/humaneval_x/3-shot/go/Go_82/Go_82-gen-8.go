    var prime bool = true
    if len(s) <= 1 {
        prime = false
    } else {
        for i := 2; i < len(s); i++ {
            if len(s)%i == 0 {
                prime = false
            }
        }
    }
    return prime
}