```go
func CarRaceCollision(n int) int {
    var collisions int
    for i := 1; i <= n; i++ {
        for j := 1; j <= n; j++ {
            if i+j <= n {
                collisions++
            }
        }
    }
    return collisions
}
```


Here is a simple Python solution:

```python
def car_race_collision(n):
    return n*(n+1)//2
```
This function calculates the total number of collisions as per the problem statement. It can be proved that the number of collisions is equal to the sum of the first n natural numbers, which is n*(n+1)//2. This is because each collision is a pair of cars moving in opposite directions, and the number of such pairs is equal to the sum of the first n natural numbers. The function returns the total number of collisions.