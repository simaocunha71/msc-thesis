for i, x := range numbers {
    for _, y := range numbers[i+1:] {
        if math.Abs(x-y) < threshold {
            return true
        }
    }
}
return false

}
