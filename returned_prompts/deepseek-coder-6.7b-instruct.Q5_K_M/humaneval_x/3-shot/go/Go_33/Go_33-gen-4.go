    divisible_by_three := make([]int, 0)
    for i := range l {
        if i%3 == 0 {
            divisible_by_three = append(divisible_by_three, l[i])
        }
    }
    sort.Ints(divisible_by_three)

    j := 0
    for i := range l {
        if i%3 == 0 {
            l[i] = divisible_by_three[j]
            j++
        }
    }

    return l
}



