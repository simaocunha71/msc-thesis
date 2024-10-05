    result := 0
    for i := 1; i <= n; i++ {
        if (i*i-i+1)%3 == 0 {
            result += 1
        }
    }
    return result
}



