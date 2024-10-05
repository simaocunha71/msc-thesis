This is a classic problem that involves counting the number of collisions between two sets of cars moving in opposite directions. The solution involves using the concept of modulo operations and the fact that the cars are infinitely sturdy and strong, meaning they do not stop after a collision.

The idea is to treat the road as a circle, where the cars that are moving left to right are wrapping around from the right to the left, and vice versa. This allows us to simplify the problem by considering only the collisions between the cars that are moving in the same direction.

Here is a simple solution in Java:
```java
public int carRaceCollision(int n) {
    return n * (n - 1) / 2;
}
```
This solution uses the formula for the number of combinations of n items taken 2 at a time, which is n*(n-1)/2. This represents the number of possible collisions between the two sets of cars.

The reason this works is that each car has a unique position on the road, and each collision involves two cars. By counting the number of combinations of cars, we are effectively counting the number of possible collisions.

Note that this solution assumes that the cars are moving at the same speed and that the road is infinitely long. It also assumes that the cars do not stop after a collision, but rather continue moving in their trajectory.

It's worth noting that this problem is a classic example of a combinatorial problem, and the solution involves using combinatorial techniques to count the number of possible collisions. The problem is also a great example of how to simplify a complex problem by treating it as a circle, which allows us to use modulo operations to simplify the problem.