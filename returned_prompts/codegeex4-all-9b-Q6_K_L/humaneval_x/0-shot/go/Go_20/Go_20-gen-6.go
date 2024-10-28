package main

import "fmt"

func FindClosestElements(numbers []float64) [2]float64 {
    minDiff := float64(1<<63 - 1)
    result := [2]float64{}
    for i := 0; i < len(numbers)-1; i++ {
        diff := numbers[i+1] - numbers[i]
        if diff < minDiff {
            minDiff = diff
            result[0] = numbers[i]
            result[1] = numbers[i+1]
        }
    }
    return result
}

func main() {
    fmt.Println(FindClosestElements([]float64{1.0, 2.0, 3.0, 4.0, 5.0, 2.2})) // (2.0, 2.2)
    fmt.Println(FindClosestElements([]float64{1.0, 2.0, 3.0, 4.0, 5.0, 2.0})) // (2.0, 2.0)
}

