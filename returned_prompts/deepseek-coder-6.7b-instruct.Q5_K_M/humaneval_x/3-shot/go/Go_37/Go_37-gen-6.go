    // Make a new array to hold the values at the even indicies
    even_indicies := make([]int, 0)
    for i := 0; i < len(l); i += 2 {
        even_indicies = append(even_indicies, l[i])
    }

    // Sort the array of even indicies
    sort.Ints(even_indicies)

    // Replace the values at the even indicies with the sorted values
    for i := 0; i < len(l); i += 2 {
        l[i] = even_indicies[i/2]
    }

    return l
}



