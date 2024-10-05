func LargestSmallestIntegers(lst []int) [2]interface{}{
    var negatives []int
    var positives []int
    for _, i := range lst {
        if i < 0 {
            negatives = append(negatives, i)
        } else if i > 0 {
            positives = append(positives, i)
        }
    }
    if len(negatives) == 0 {
        negatives = nil
    } else {
        negatives = []int{negatives[len(negatives)-1]}
    }
    if len(positives) == 0 {
        positives = nil
    } else {
        positives = []int{positives[0]}
    }
    return [2]interface{}{negatives, positives}
}