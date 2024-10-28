    odd_count := 0
    for _, num := range lst1 {
        if num % 2 != 0 {
            odd_count += 1
        }
    }
    even_count := len(lst2) - odd_count
    if odd_count > even_count {
        return "NO"
    }
    return "YES"
}



