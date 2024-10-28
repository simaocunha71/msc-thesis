```go
func CarRaceCollision(n int) int {
    ans := 0
    for i := 1; i <= n; i++ {
        for j := 1; j <= n; j++ {
            if i != j {
                ans += 2 * (i - 1) * (n - j)
            }
        }
    }
    return ans
}
```

Explanation:
In this problem, we are asked to find the number of collisions that will occur between n cars moving in opposite directions. We can model this problem as a combinatorics problem, where we are counting the number of pairs of cars that will collide.

Let's first consider a single car moving from left to right. It will collide with all cars moving from right to left that are to its left. The number of such cars is (n - 1), since we are not considering the current car.

Now, let's consider another car moving from left to right. It will collide with all cars moving from right to left that are to its right. The number of such cars is also (n - 1).

Notice that both cars have collided with the same set of cars, but in a different order. This means that we have double-counted the number of collisions. To avoid this, we need to divide the total number of collisions by 2.

The above logic can be applied to all cars moving from left to right. Therefore, the total number of collisions is:

(n - 1) + (n - 2) + ... + 1 = n * (n - 1) / 2

This is the number of collisions for one direction. Since there are n cars moving in each direction, the total number of collisions is:

2 * n * (n - 1) / 2 = n * (n - 1)

However, this is the number of collisions when all cars are considered. But we are asked to find the number of collisions when all cars are not considered. Therefore, we need to subtract the number of collisions when all cars are considered from the total number of collisions.

The number of collisions when all cars are considered is:

1 * (n - 1) + 2 * (n - 2) + ... + (n - 1) = n * (n - 1)

Therefore, the number of collisions when all cars are not considered is:

n * (n - 1) - n * (n - 1)