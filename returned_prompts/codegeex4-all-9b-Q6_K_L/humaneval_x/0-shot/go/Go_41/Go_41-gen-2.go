You can solve this problem using a simple simulation. Here's a possible solution in Go:

```go
func CarRaceCollision(n int) int {
    leftCars := make([]int, n)
    rightCars := make([]int, n)

    // Initialize the positions of the cars
    for i := 0; i < n; i++ {
        leftCars[i] = i
        rightCars[i] = n + i
    }

    collisions := 0

    // Simulate the movement of the cars
    for {
        // Check for collisions
        for i := 0; i < n; i++ {
            if leftCars[i] >= rightCars[i] {
                collisions++
                leftCars[i]++
                rightCars[i]++
            }
        }

        // Check if all cars have passed each other
        allPassed := true
        for i := 0; i < n; i++ {
            if leftCars[i] < rightCars[i] {
                allPassed = false
                break
            }
        }

        if allPassed {
            break
        }
    }

    return collisions
}
```

This solution uses two arrays, `leftCars` and `rightCars`, to store the positions of the cars moving left and right, respectively. It then simulates the movement of the cars and checks for collisions until all cars have passed each other.

The function `CarRaceCollision` takes an integer `n` as input, which represents the number of cars moving in each direction. It returns the number of collisions that occurred.

Note that this solution assumes that the cars start at positions 0 and `n`, and that they move in the same speed.