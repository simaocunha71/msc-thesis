The problem can be solved using a simple mathematical approach. The key idea is to find the number of collisions that will occur between the two sets of cars. The cars are moving in the same speed, so the collisions will occur when the left-moving cars catch up to the right-moving cars.

Let's say the distance between the two sets of cars is x. The left-moving cars will travel x distance in x seconds, and the right-moving cars will travel x distance in x seconds as well. Since the cars are traveling in the same speed, the left-moving cars will catch up to the right-moving cars in x seconds.

Now, let's consider the left-moving cars that are x distance behind the right-moving cars. In x seconds, these cars will travel x distance and catch up to the right-moving cars. However, the right-moving cars will also travel x distance in x seconds, so the left-moving cars will not catch up to the right-moving cars in this case.

Therefore, the number of collisions that will occur is the number of left-moving cars that are x distance behind the right-moving cars. This can be calculated using the formula:

collisions = n * (n-1) / 2

This is because there are n left-moving cars, and each car will collide with (n-1) other cars.

Here is the Java code that implements this solution:
```java
public int carRaceCollision(int n) {
    return n * (n-1) / 2;
}
```
This code takes an integer n as input and returns the number of collisions that will occur. The time complexity of this solution is O(1) because it only involves a constant number of operations. The space complexity is O(1) because it only uses a constant amount of space to store the result.