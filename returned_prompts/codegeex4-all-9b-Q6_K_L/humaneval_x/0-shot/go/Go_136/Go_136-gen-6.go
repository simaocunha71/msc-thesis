package kata

func LargestSmallestIntegers(lst []int) [2]interface{} {
    var negMax, posMin interface{}
    for _, i := range lst {
        if i < 0 {
            if negMax == nil || i > negMax.(int) {
                negMax = i
            }
        }
        if i > 0 {
            if posMin == nil || i < posMin.(int) {
                posMin = i
            }
        }
    }
    return [2]interface{}{negMax, posMin}
}