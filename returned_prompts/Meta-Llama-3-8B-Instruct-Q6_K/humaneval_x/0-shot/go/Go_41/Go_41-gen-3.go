```go
func CarRaceCollision(n int) int {
    collisions := 0
    for i := 1; i <= n; i++ {
        for j := 1; j <= n; j++ {
            if i != j {
                collisions += 1
            }
        }
    }
    return collisions
}
```


Explanation:
The problem can be solved by calculating the total number of possible pairs of cars that could collide. Since there are `n` cars moving left to right and `n` cars moving right to left, the total number of possible pairs is `n * n`. However, this includes pairs of cars that are the same, i.e., the same car moving in both directions. Since the problem states that two cars are said to collide when a car that's moving left to right hits a car that's moving right to left, we need to subtract the pairs of cars that are the same.

In the given code, the outer loop runs from 1 to `n`, and the inner loop also runs from 1 to `n`. The condition `i != j` ensures that we don't count the pairs of cars that are the same. The variable `collisions` is incremented by 1 for each pair of cars that could collide, and the final result is returned.

This solution has a time complexity of O(n^2) and a space complexity of O(1), as it only uses a constant amount of space to store the result. This is because the problem requires calculating the total number of possible pairs of cars that could collide, which is a quadratic operation. The space complexity is constant because we only use a single variable to store the result.