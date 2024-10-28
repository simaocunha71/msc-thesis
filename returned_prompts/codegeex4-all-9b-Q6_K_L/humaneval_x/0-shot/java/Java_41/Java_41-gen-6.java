You can use a formula to solve this problem. The number of collisions is given by the formula n*(n-1)/2, where n is the number of cars. This formula comes from the fact that each car can collide with n-1 other cars, and each pair of cars can only collide once. Therefore, the total number of collisions is n*(n-1)/2. Here is the code:

```java
public int carRaceCollision(int n) {
    return n * (n - 1) / 2;
}
```

This code simply calculates the number of collisions using the given formula and returns the result.