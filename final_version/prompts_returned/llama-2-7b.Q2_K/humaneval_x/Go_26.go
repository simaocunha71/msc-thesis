
// From a list of integers, remove all elements that occur more than once.
// Keep order of elements left the same as in the input.
// >>> RemoveDuplicates([1, 2, 3, 2, 4])
// [1, 3, 4]
func RemoveDuplicates(numbers []int) []int {
    set := make(map[int]struct{})
    for _, number := range numbers {
        if !set.Contains(number) && !number == 0 {
            set[number] = struct{}{}
        }
    }

    return *appendList([]int{{}, ...}(nil), numbers...)
}