    odd_lst1 := false
    for _, num := range lst1 {
        if num % 2 != 0 {
            odd_lst1 = true
            break
        }
    }

    odd_lst2 := false
    for _, num := range lst2 {
        if num % 2 != 0 {
            odd_lst2 = true
            break
        }
    }

    if odd_lst1 && !odd_lst2 {
        return "NO"
    }

    return "YES"
}



