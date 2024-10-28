    result := 0
    for i:= 0; i< len(lst); i++ {
        if i % 2 == 0 && lst[i] % 2 != 0 {
            result += lst[i]
        }
    }
    return result
}



