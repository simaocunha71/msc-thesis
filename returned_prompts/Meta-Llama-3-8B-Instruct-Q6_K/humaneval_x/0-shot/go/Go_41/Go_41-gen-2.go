```go
func CarRaceCollision(n int) int {
    var res int
    for i := 1; i <= n; i++ {
        for j := 1; j <= n; j++ {
            if i != j {
                res++
            }
        }
    }
    return res
}
```


The above code calculates the number of collisions by iterating over all possible pairs of cars. Since the cars are moving at the same speed and are infinitely sturdy, each car will collide with all other cars except itself. Therefore, the number of collisions is given by the formula n*(n-1)/2. The above code, however, uses a brute force approach and is not efficient. It calculates the number of collisions as n*(n-1) and then returns it. The time complexity of this code is O(n^2), which is not efficient for large values of n. 

Here is a more efficient solution:

```go
func CarRaceCollision(n int) int {
    return n * (n - 1) / 2
}
```

This solution calculates the number of collisions using the formula n*(n-1)/2, which is the mathematical formula for the number of combinations of n items taken 2 at a time. This solution has a time complexity of O(1), which is much more efficient than the previous solution. 

The above code takes advantage of the mathematical property of the number of combinations, which is that it can be calculated using the formula n*(n-1)/2. This property is used to calculate the number of collisions, which is the number of combinations of n cars taken 2 at a time. The code is simple and efficient, and it has a time complexity of O(1). 

This solution is more efficient and easier to understand than the previous one. It directly calculates the number of collisions using the mathematical formula, without using a brute force approach. The time complexity of this code is O(1), which is much more efficient than the previous solution. 

This code is also more robust and can handle large values of n, whereas the previous code may run out of memory or take a long time to execute for large values of n. 

In conclusion, the above code is a more efficient and easier to understand solution that calculates the number of collisions in a car race. It uses the mathematical formula for the number of combinations to calculate the number of collisions, and it has a time complexity of O(1). 

Note that the formula n