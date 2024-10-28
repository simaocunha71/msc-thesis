    odd_lst1 := 0
    odd_lst2 := 0

    for _, num := range lst1 {
        if num % 2 != 0 {
            odd_lst1++
        }
    }

    for _, num := range lst2 {
        if num % 2 != 0 {
            odd_lst2++
        }
    }

    if odd_lst1 <= odd_lst2 {
        return "YES"
    }else{
        return "NO"
    }
}



