    sum := 0
    for index, value := range lst {
        if index % 3 == 0 {
            sum += int(math.Pow(float64(value), 2))
        } else if index % 4 == 0 {
            sum += int(math.Pow(float64(value), 3))
        } else {
            sum += value
        }
    }
    return sum
}

This function works by iterating over the list of integers (lst). For each entry, it checks whether the index is a multiple of 3 or 4. If the index is a multiple of 3, the function squares the value and adds it to the sum. If the index is a multiple of 4 but not 3, the function cubes the value and adds it to the sum. If the index is not a multiple of 3 or 4, the function just adds the value to the sum. Finally, the function returns the sum of all entries.

Example:

lst := []int{1, 2, 3}
fmt.Println(SumSquares(lst)) // Output: 6

lst := []int{}
fmt.Println(SumSquares(lst)) // Output: 0

lst := []int{-1, -5, 2, -1, -5}
fmt.Println(SumSquares(lst)) // Output: -126

This function correctly handles lists of any length and correctly handles negative values.
*/

// This function will take a list of integers. For all entries in the list, the function shall square the integer entry if its index is a
// multiple of 3 and will cube the integer entry if its index is a multiple of