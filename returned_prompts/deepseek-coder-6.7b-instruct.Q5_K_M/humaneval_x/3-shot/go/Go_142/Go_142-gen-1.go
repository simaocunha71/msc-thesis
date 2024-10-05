    sum := 0
    for i, num := range lst {
        if (i+1)%3 == 0 && (i+1)%4 !=0 {
            sum += int(math.Pow(float64(num), 2))
        } else if (i+1)%4 == 0 && (i+1)%3 !=0 {
            sum += int(math.Pow(float64(num), 3))
        } else {
            sum += num
        }
    }
    return sum
}



