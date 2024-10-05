
    // Initialize a counter for the number of odd elements in lst1.
    oddCount := 0

    // Initialize a counter for the number of elements exchanged.
    exchangedCount := 0

    // Initialize a boolean flag to track whether all the elements of lst1 are even.
    allEven := true

    // Initialize an empty list to store the elements of lst2 that are odd.
    oddElements := []int{}

    // Iterate over the elements of lst1.
    for _, elem := range lst1 {
        // Check whether the element is odd or even.
        if elem % 2 != 0 {
            // Increment the counter for odd elements in lst1.
            oddCount++

            // Decrement the counter for the number of elements exchanged.
            exchangedCount--

            // Set the flag to false.
            allEven = false
        } else {
            // Increment the counter for the number of elements exchanged.
            exchangedCount++
        }
    }

    // Iterate over the elements of lst2.
    for _, elem := range lst2 {
        // Check whether the element is odd or even.
        if elem % 2 != 0 {
            // Check whether the counter for odd elements in lst1 is greater than the counter for the number of elements exchanged.
            if oddCount > exchangedCount {
                // Increment the counter for the number of elements exchanged.
                exchangedCount++

                // Decrement the counter for odd elements in lst1.
                oddCount--

                // Increment the counter for the odd elements in lst2.
                oddElements = append(oddElements, elem)
            }
        }
    }

    // Check whether all the elements of lst1 are even.
    if allEven {
        return "YES"
    }

    // Check whether all the elements of lst1 are odd.
    if oddCount == 0 {
        return "NO"
    }

    // Check whether all the elements of lst1 are odd.
    if oddElements != nil {
        return "YES"
   