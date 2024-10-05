```go
func CarRaceCollision(n int) int {
    // Initialize the number of collisions to 0
    collisions := 0

    // Loop through all the cars
    for i := 0; i < n; i++ {
        // Check if the current car collides with any other car
        for j := i + 1; j < n; j++ {
            // If the current car is moving left to right and the other car is moving right to left,
            // then they collide
            if i < j {
                collisions++
            }
        }
    }

    // Return the number of collisions
    return collisions
}
```
