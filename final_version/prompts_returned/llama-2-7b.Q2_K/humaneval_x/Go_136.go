
// Create a function that returns a tuple (a, b), where 'a' is
// the largest of negative integers, and 'b' is the smallest
// of positive integers in a list.
// If there is no negative or positive integers, return them as nil.
// 
// Examples:
// LargestSmallestIntegers([2, 4, 1, 3, 5, 7]) == (nil, 1)
// LargestSmallestIntegers([]) == (nil, nil)
// LargestSmallestIntegers([0]) == (nil, nil)
func LargestSmallestIntegers(lst []int) [2]interface{}{
    if len(lst) == 0 {
        return [2]interface{}{nil, nil}
    }

    large, small := nil, nil
    for idx, v := range lst {
        // 对于每个下标 i，如果 v[i] > max 或者如果 v[i] < min。
        if large == nil || large.(float64) <= v.(float64) && small == nil || small.(float64) >= v.(float64) {
            large = &v
            small = nil
        }
    }
    return [2]interface{}{large, small}
}