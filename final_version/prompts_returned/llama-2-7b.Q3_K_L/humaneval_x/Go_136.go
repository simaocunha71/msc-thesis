
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
        return [2]interface{}{}
    }else{
        max := -1e9
        min := 1e9
        
        for _, v := range lst {
            if v < min {
                min = v
            } else if v > max {
                max = v
            }
        }
    
        return [2]interface{}{min,max}
    }
}