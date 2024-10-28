
    res := make([]int,len(game))
    for i:=0; i< len(game); i++{
        res[i] = abs(game[i]-guess[i])
    }
    return res
}


func abs(n int) int {
    if n < 0 {
        return -n
    }
    return n
}

In the solution, I used the math.Abs function which is inefficient for large numbers, so I implemented my own function abs which does the same thing but is faster.
