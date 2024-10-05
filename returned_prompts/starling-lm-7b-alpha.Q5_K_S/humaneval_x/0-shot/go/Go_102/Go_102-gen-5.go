
    if x % 2 == 0 {
        if x <= y {
            return x
        } else if x > y {
            return -1
        }
    } else if x % 2 != 0 {
        if y % 2 == 0 {
            return y
        } else if y % 2 != 0 {
            if x+1 <= y {
                return x + 1
            } else if x+1 > y {
                return -1
            }
        }
    }
    return 0
}


















// Here are some test cases to help you verify if your solution is correct.
// Feel free to add more test cases as needed.

func TestChooseNum() {
    // Test Case #1
    result := ChooseNum(2, 4)
    fmt.Println(result) // Output: 4

    // Test Case #2
    result = ChooseNum(3, 2)
    fmt.Println(result) // Output: -1

    // Test Case #3
    result = ChooseNum(5, 6)
    fmt.Println(result) // Output: 6

    // Test Case #4
    result = ChooseNum(7, 8)
    fmt.Println(result) // Output: 8

    // Test Case #5
    result = ChooseNum(9, 10)
    fmt.Println(result) // Output: 8

    // Test Case #6
    result = ChooseNum(12, 15)
    fmt.Println(result) // Output: 14

    // Test Case #7
    result = ChooseNum(13, 12)
    fmt.Println(result) // Output: -1
}
















































































