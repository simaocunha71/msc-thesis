
    min, max := math.Inf(1), -math.Inf(1)

    for _, num := range numbers {
        if num < min {
            min = num
        }
        if num > max {
            max = num
        }
    }

    rescale := make([]float64, len(numbers))

    for i, num := range numbers {
        rescale[i] = (num - min) / (max - min)
    }

    return rescale
}




// Given list of numbers  (of at least two elements), return the median of the list.
// 
// >>> Median([1.0, 2.0, 3.0, 4.0, 5.0])
// 3.0
// 
// >>> Median([1.0, 2.0, 3.0, 4.0])
// 2.5
func Median(numbers []float64) float64 {

    sortedNumbers := make([]float64, len(numbers))
    copy(sortedNumbers, numbers)
    sort.Float64s(sortedNumbers)

    n := len(sortedNumbers)

    if n % 2 == 0 {
        return (sortedNumbers[n/2-1] + sortedNumbers[n/2]) / 2.0
    } else {
        return sortedNumbers[n/2]
    }
}




// Given a list of numbers, return the mean of those numbers.
// 
// >>> Mean([1.0, 2.0, 3.0, 4.0, 5.0])
// 3.0
func Mean(numbers []float64) float64 {

    sum := 0.0

    for _, num := range numbers {
        sum += num
    }

    return sum / float64(len(numbers))
}




// Given a string, return a string where all characters are lowercase and all words are separated by hyphens.
// 
