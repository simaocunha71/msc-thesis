    divisible_by_three := make([]int, 0)
    for i  := 0; i < len(l); i += 3 {
        divisible_by_three = append(divisible_by_three, l[i])
    }

    sort.Ints(divisible_by_three)

    j  := 0
    for i  := 0; i < len(l); i += 3 {
        l[i] = divisible_by_three[j]
        j += 1
    }

    return l
}



