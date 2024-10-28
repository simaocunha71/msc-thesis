    divisibleByThreeIdx := make([]int, 0)
    for i := range l {
        if (i+1) % 3 == 0 {
            divisibleByThreeIdx = append(divisibleByThreeIdx, l[i])
        }
    }
    sort.Ints(divisibleByThreeIdx)

    j := 0
    for i := range l {
        if (i+1) % 3 == 0 {
            l[i] = divisibleByThreeIdx[j]
            j++
        }
    }
    return l
}



