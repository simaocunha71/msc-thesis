    even_count := 0
    odd_count := 0
    for _, v := range lst1 {
        if v % 2 == 0 {
            even_count += 1
        }else {
            odd_count += 1
        }
    }

    for _, v := range lst2 {
        if v % 2 == 0 {
            even_count += 1
        }else {
            odd_count += 1
        }
    }

    if odd_count >= even_count {
        return "NO"
    }else {
        return "YES"
    }
}



