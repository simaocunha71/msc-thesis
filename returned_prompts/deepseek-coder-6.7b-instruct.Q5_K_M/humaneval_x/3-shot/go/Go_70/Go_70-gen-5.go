    sort.Ints(lst)
    length := len(lst)

    if length % 2 == 0 {
        for i := 0; i < length/2; i += 2 {
            lst[i], lst[length-i-1] = lst[length-i-1], lst[i]
        }
    } else {
        for i := 0; i < length/2; i += 2 {
            lst[i], lst[length-i-1] = lst[length-i-1], lst[i]
        }
    }

    return lst
}



