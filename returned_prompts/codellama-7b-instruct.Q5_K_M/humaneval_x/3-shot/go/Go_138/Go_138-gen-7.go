    for i := 0; i < 100; i++ {
        if i%2 != 0{
            continue
        }

        if i+i+i+i == n{
            return true
        }
    }
    return false
}



