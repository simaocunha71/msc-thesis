    if len(xs)%2==0 && xs[0] != 0 {
        root := 0.0
        for i := 0; i < len(xs); i++ {
            root += float64(xs[i]) * math.Pow(-1, i) / math.Pow(float64(len(xs)-1), float64(i))
        }
        return root
    } else {
        return 0.0
    }
} 



