Here is a Java solution for the problem:

```java
public int carRaceCollision(int n) {
    return (n * (n - 1)) / 2;
}
```

Explanation:
This solution is based on the fact that each car that's moving left to right can potentially collide with each car that's moving right to left. Thus, if there are n cars moving left to right and n cars moving right to left, there would be n * n possible collisions. However, since each pair of cars can only collide once, we need to divide by 2 to get the correct answer. This results in the formula (n * (n - 1)) / 2. 

This formula takes into account the fact that the first car moving left to right can only collide with n-1 cars moving right to left, the second car can only collide with n-2 cars moving right to left, and so on. This results in a total of n * (n - 1) / 2 collisions.