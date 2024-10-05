    for i, j := 0, 0; i < len(l1) && j < len(l2); {
        if l1[i] == l2[j] {
            i++
            j++
        } else if l1[i] < l2[j] {
            i++
        } else {
            j++
        }
    }

    return l1[:i]
}

// Return sorted unique Common elements for two lists.
// >>> Common([1, 4, 3, 34, 653, 2, 5], [5, 7, 1, 5, 9, 653, 121])
// [1, 5, 653]
// >>> Common([5, 3, 2, 8], [3, 2])
// [2, 3]
func Common(l1 []int,l2 []int) []int {

B:
    for i, j := 0, 0; i < len(l1) && j < len(l2); {
        if l1[i] == l2[j] {
            i++
            j++
        } else if l1[i] < l2[j] {
            i++
        } else {
            j++
        }
    }

    return l1[:i]
}

C:
    l1 = append(l1, l2...)
    sort.Ints(l1)
    last := 0
    for i := 1; i < len(l1); i++ {
        if l1[last] != l1[i] {
            l1[last+1] = l1[i]
            last++
        }
    }
    return l1[:last+1]
}

D:
    l1 = append(l1, l2...)
    sort.Ints(l1)
    last := 0
    for i := 1; i < len(l1); i++ {
        if l1[last] != l1[i] {
            l1[last+1] = l1[i]
           