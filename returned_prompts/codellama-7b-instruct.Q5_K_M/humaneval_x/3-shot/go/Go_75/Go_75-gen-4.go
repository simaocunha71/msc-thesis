    for i := 2; i < 100; i++ {
        if a%i == 0{
            for j := 2; j < 100; j++ {
                if i%j == 0{
                    if a%j == 0{
                        if i == j {
                            return false
                        }
                        if a%(i*j) == 0{
                            return true
                        }
                    }
                }
            }
        }
    }
    return false
}



