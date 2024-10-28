    result := make([]int,0)
    for i := range game{
        diff := int(math.Abs(float64(guess[i]-game[i])))
        result = append(result,diff)
    }
    return result
}