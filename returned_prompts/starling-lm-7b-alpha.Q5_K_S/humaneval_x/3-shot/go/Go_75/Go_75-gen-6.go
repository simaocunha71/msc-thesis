    if a % 2 == 0 {
        return false
    }else {
        for i := 3; i * i <= a; i += 2 {
            if a % i == 0 {
                return false
            }
        }
        return true
    }
}



