    // SortThird uses the sort.Slice() function to sort the list l.
    // sort.Slice() takes three arguments:
    // 1. The list that you want to sort
    // 2. The index of the first element to sort (inclusive)
    // 3. The index of the last element to sort (exclusive)
    // sort.Slice() returns a boolean indicating whether the list was already sorted
    // If the list was sorted, then we can return l directly
    // Otherwise, we need to sort the list and return it
    if !sort.SliceIsSorted(l, 0, len(l)) {
        sort.Slice(l, func(i, j int) bool {
            if i % 3 == 0 && j % 3 == 0 {
                return l[i] < l[j]
            }
            return true
        })
    }
    return l
}

// This function takes a list l and a function f(x) that takes an integer x and returns a boolean.
// It returns a list l' such that l' is identical to l in the indicies that are not divisible by three, while its values at the indicies that are divisible by three are
// equal to the values of the corresponding indicies of l, but sorted according to the function f(x)
// >>> SortThird([1, 2, 3], func(x){return x > 2})
// [3, 2, 1]
// >>> SortThird([5, 6, 3, 4, 8, 9, 2], func(x){return x > 2})
// [9, 6, 3, 4, 8, 5, 2]
func SortThird(l []int, f func(int) bool) []int {
    // SortThird uses the sort.Slice() function to sort the list l.
    // sort.Slice() takes three arguments:
    // 1. The list that you want to sort
    // 2. The index of the first element to sort (inclusive)
    // 3. The index of the last element to sort (exclusive)
   