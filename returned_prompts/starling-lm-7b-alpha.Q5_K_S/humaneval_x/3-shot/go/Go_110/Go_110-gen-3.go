    even_count := 0
    for _, v := range lst1 {
        if v % 2 == 0 {
            even_count += 1
        }
    }
    odd_count := len(lst1) - even_count
    for _, v := range lst2 {
        if v % 2 == 1 {
            odd_count -= 1
        }
    }
    if odd_count < 0 {
        return "NO"
    }
    return "YES"
}



