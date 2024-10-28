    for i := 0; i < len(lst)-1; i++ {
        if lst[i] >= lst[i+1] {
            if i > 0 && lst[i] == lst[i-1] {
                return false
            }
            return false
        }
    }
    return true
} 



