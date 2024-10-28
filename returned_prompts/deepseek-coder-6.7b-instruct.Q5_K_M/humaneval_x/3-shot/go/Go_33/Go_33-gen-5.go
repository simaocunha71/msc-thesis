    sorted_third := make([]int,0)
    for i := 2; i < len(l); i += 3 {
        sorted_third = append(sorted_third, l[i])
    }

    sort.Ints(sorted_third)

    j := 0
    for i := 2; i < len(l); i += 3 {
        l[i] = sorted_third[j]
        j++
    }

    return l
}



