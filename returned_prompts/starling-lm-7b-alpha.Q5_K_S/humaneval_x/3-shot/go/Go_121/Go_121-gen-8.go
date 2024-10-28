    result := 0
    for i := 0; i < len(lst); i++ {
        if lst[i]%2==0 && i%2==0 {
            result += lst[i]
        }
    }
    return result
}



