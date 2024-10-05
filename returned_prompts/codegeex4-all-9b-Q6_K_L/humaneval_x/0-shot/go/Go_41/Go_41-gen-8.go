You can solve this problem by using a simple loop. Here is the solution in Go:

```go
func CarRaceCollision(n int) int {
    return n * n
}
```

Explanation:
Since there are n cars moving left to right and n cars moving right to left, each car from one set will collide with each car from the other set. Therefore, the total number of collisions will be the product of the number of cars from each set, which is n * n.