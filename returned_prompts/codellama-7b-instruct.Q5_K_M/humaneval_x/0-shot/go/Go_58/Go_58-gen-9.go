    // Create a map to count the elements in l1 and l2
    m1 := make(map[int]int)
    m2 := make(map[int]int)

    for _, v := range l1 {
        m1[v]++
    }
    for _, v := range l2 {
        m2[v]++
    }

    // Create a slice to store the common elements
    common := make([]int, 0, len(m1) + len(m2))

    // Loop through the elements in l1 and add it to common slice if
    // it is also in l2 and the count in m1 is greater than 0 and the
    // count in m2 is greater than 0.
    for k, v := range m1 {
        if v > 0 && m2[k] > 0 {
            common = append(common, k)
        }
    }
    return common
}
