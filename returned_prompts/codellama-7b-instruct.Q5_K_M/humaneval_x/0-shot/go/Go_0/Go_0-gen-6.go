for i, n := range numbers {
    for _, m := range numbers[i+1:] {
        if math.Abs(m-n) < threshold {
            return true
        }
    }
}

return false
}


