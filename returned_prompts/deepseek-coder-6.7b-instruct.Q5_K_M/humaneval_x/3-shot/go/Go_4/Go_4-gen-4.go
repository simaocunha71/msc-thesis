    var sum float64=0
    var mean float64=0
    var deviation float64=0
    for  _, number := range numbers {
        sum += number
    }
    mean=sum/float64(len(numbers))
    for  _, number := range numbers {
        deviation += math.Abs(number-mean)
    }
    return deviation/float64(len(numbers))
}



