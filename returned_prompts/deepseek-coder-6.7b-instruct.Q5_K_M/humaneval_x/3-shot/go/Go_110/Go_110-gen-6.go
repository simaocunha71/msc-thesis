    odd_in_lst1 := 0
    for _, num := range lst1 {
        if num % 2 != 0 {
            odd_in_lst1++
        }
    }

    even_in_lst2 := 0
    for _, num := range lst2 {
        if num % 2 == 0 {
            even_in_lst2++
        }
    }

    if odd_in_lst1 <= even_in_lst2 {
        return "YES"
    }
    return "NO"
}



