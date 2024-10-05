    str := strconv.Itoa(int(math.Abs(float64(num))))

    var even, odd int
    for _, c := range str {
        if (c-'0')%2 == 0 {
            even++
        } else {
            odd++
        }
    }

    return [2]int{even, odd}
}



