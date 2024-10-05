    odd_lst1_count := 0
    for _, i := range lst1 {
        if i % 2 != 0 {
            odd_lst1_count += 1
        }
    }

    odd_lst2_count := 0
    for _, i := range lst2 {
        if i % 2 != 0 {
            odd_lst2_count += 1
        }
    }

    if odd_lst1_count > odd_lst2_count {
        return "NO"
    }

    return "YES"
}



