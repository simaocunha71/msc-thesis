    if n % 2 != 0 {
        return false
    }
    for i := 2; i < n/2; i += 2 {
        if IsEqualToSumEven(n-i) {
            return true
        }
    }
    return false
}



