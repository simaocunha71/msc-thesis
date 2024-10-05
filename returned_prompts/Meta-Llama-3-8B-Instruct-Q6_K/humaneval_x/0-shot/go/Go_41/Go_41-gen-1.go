```
func CarRaceCollision(n int) int {
    collisions := 0
    for i := 1; i <= n; i++ {
        for j := 1; j <= n; j++ {
            if i+j <= 2*n && i+j > 0 {
                collisions++
            }
        }
    }
    return collisions
}
```
Explanation:
The problem asks to find the number of collisions between cars moving in opposite directions. Since the cars are infinitely sturdy and strong, they do not change their direction after a collision. This means that the number of collisions is simply the number of pairs of cars that can intersect with each other.

We can model this situation using two nested loops, where the outer loop represents the cars moving left to right and the inner loop represents the cars moving right to left. We increment the collision counter whenever the sum of the two indices is less than or equal to 2n (since the maximum number of cars that can intersect is 2n) and greater than 0 (since the cars cannot intersect with themselves).

The time complexity of this solution is O(n^2), since we are iterating over each pair of cars. The space complexity is O(1), since we are using a constant amount of space to store the collision counter.