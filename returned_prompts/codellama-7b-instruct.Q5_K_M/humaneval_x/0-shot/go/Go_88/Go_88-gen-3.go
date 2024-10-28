    // sort the array in ascending order
    sort.Ints(array)

    // check if the sum of the first and last index values is odd
    if array[0] + array[len(array)-1]%2 == 1 {

        // if the sum is odd, reverse the sorted array
        sort.Ints(array)
        return array
    }

    // sort the array in descending order
    sort.Sort(sort.Reverse(sort.IntSlice(array)))
    return array
}

B:
    // sort the array in ascending order
    sort.Ints(array)

    // check if the sum of the first and last index values is even
    if array[0] + array[len(array)-1]%2 == 0 {

        // if the sum is even, reverse the sorted array
        sort.Ints(array)
        return array
    }

    // sort the array in descending order
    sort.Sort(sort.Reverse(sort.IntSlice(array)))
    return array
}

C:
    // sort the array in ascending order
    sort.Ints(array)

    // check if the sum of the first and last index values is odd
    if array[0] + array[len(array)-1]%2 == 1 {

        // if the sum is odd, reverse the sorted array
        sort.Ints(array)
        return array
    }

    // sort the array in descending order
    sort.Sort(sort.Reverse(sort.IntSlice(array)))
    return array
}

D:
    // sort the array in ascending order
    sort.Ints(array)

    // check if the sum of the first and last index values is even
    if array[0] + array[len(array)-1]%2 == 0 {

        // if the sum is even, reverse the sorted array
        sort.Ints(array)
        return array
    }

    // sort the array in descending order
    sort.Sort(sort.Reverse(sort.IntSlice(array)))
    return array
}

E:
