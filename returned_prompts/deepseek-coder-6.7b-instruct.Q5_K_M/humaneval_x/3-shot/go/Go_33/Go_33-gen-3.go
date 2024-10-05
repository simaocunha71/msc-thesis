    divisibleByThree := make([]int, 0)
    for i := 2; i < len(l); i += 3 {
        divisibleByThree = append(divisibleByThree, l[i])
    }
    sort.Ints(divisibleByThree)

    for i, j := 2, 0; i < len(l); i += 3 {
        l[i] = divisibleByThree[j]
        j++
    }
    return l
}



