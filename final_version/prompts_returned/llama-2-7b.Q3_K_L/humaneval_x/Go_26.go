
// From a list of integers, remove all elements that occur more than once.
// Keep order of elements left the same as in the input.
// >>> RemoveDuplicates([1, 2, 3, 2, 4])
// [1, 3, 4]
func RemoveDuplicates(numbers []int) []int {
    var nums = make([]int, len(numbers))
    for i, v := range numbers{
        if _, ok := nums[v]; ok != true {
            nums = append(nums, v)
        } else {
            continue
        }
    }
    return nums
}