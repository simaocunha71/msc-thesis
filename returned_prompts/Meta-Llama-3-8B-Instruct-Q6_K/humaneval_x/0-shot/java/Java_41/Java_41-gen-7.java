The problem is asking you to find the number of collisions that will occur in a road where n cars are driving from left to right and n cars are driving from right to left. The cars are moving at the same speed and they are infinitely sturdy and strong, so they will not stop or change direction after a collision. The collision will only affect the distance between the two cars, not their speed.

The key to this problem is to realize that the number of collisions will be equal to the number of pairs of cars that are moving in opposite directions and will eventually meet each other. This is because each collision will create a new pair of cars that will eventually meet each other, and the cars that collided will continue moving in their original directions.

To solve this problem, you can use the concept of modular arithmetic. The idea is to consider the relative positions of the cars as they move. Since the cars are moving at the same speed, the relative positions of the cars will repeat every n units of distance. Therefore, you can find the number of collisions by finding the number of pairs of cars that will eventually meet each other.

Here is the Java code to solve this problem:

```java
public int carRaceCollision(int n) {
    return n * (n - 1) / 2;
}
```

This code calculates the number of collisions by using the formula for the number of pairs of items in a set, which is n * (n - 1) / 2. This formula is used because each car can collide with every other car except itself, and there are n cars.

The time complexity of this code is O(1) because it only involves a constant number of operations. The space complexity is O(1) because it only uses a constant amount of space to store the result.