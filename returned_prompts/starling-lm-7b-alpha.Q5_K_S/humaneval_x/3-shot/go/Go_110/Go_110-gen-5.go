    odd_elements_needed := 0
    for _, v := range lst1 {
        if v % 2 != 0 {
            odd_elements_needed += 1
        }
    }
    odd_elements_available := 0
    for _, v := range lst2 {
        if v % 2 != 0 {
            odd_elements_available += 1
        }
    }
    if odd_elements_available >= odd_elements_needed {
        return "YES"
    } else {
        return "NO"
    }
}



