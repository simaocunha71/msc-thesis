    for _, char := range s {
        switch strings.ToLower(string(char)) {
        case "a", "e", "i", "o", "u":
            continue A
        }
    }

    return len(s)
}

// Write a function Max which takes two integers as input and returns
// the greater value between the two.
// 
// Example:
// >>> Max(1, 2)
// 2
// >>> Max(3, 2)
// 3
func Max(a int, b int) int {
    if a > b {
        return a
    }
    return b
}

// Write a function Abs which takes an integer as input and returns
// its absolute value.
// 
// Example:
// >>> Abs(-3)
// 3
// >>> Abs(3)
// 3
func Abs(a int) int {
    if a > 0 {
        return a
    }
    return -a
}

// Write a function Sqrt which takes a float64 as input and returns
// its square root.
// 
// Example:
// >>> Sqrt(9)
// 3
// >>> Sqrt(16)
// 4
func Sqrt(a float64) float64 {
    return math.Sqrt(a)
}

// Write a function Sum which takes a slice of integers as input and
// returns the sum of all the integers in the slice.
// 
// Example:
// >>> Sum([]int{1, 2, 3, 4, 5})
// 15
// >>> Sum([]int{1, 2, 3, 4, 5, 6, 7, 8, 9})
// 45
func Sum(s []int) int {
    sum := 0
    for _, i := range s {
        sum += i
    }
    return sum
}

// Write a function Len which takes a slice as input and returns its
// length.
// 
// Example:
// >>> Len([]string{"a", "b", "c"})
// 3
// >>> Len(