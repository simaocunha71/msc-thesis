    var divisibleByThree []int
    for i := range l  {
        if i%3 == 0  {
            divisibleByThree = append(divisibleByThree, l[i])
        }
    }
    sort.Ints(divisibleByThree)

    j := 0
    for i := range l  {
        if i%3 == 0  {
            l[i] = divisibleByThree[j]
            j++
        }
    }
    return l
}

