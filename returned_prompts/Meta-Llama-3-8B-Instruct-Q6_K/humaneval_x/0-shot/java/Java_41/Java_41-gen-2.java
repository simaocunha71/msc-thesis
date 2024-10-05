The problem is asking for the number of collisions between two sets of cars moving in opposite directions. The cars are infinitely sturdy and strong, so they don't stop after a collision, but instead continue moving in their original direction.

To solve this problem, we can use a simple formula: the number of collisions is equal to the number of pairs of cars that will cross each other's path.

The number of pairs of cars that will cross each other's path is given by the formula:

n * (n - 1) / 2

This is because each car can potentially collide with all the cars in the opposite direction, except itself. So, we multiply the number of cars by the number of cars minus one, and then divide by two to account for the fact that we're counting each pair twice.

Here's the code:

```java
public int carRaceCollision(int n) {
    return n * (n - 1) / 2;
}
```

This code will return the correct number of collisions for any given number of cars. For example, if there are 3 cars, the function will return 3, because each car can potentially collide with the other two cars. If there are 4 cars, the function will return 6, because each car can potentially collide with the other three cars. And so on.