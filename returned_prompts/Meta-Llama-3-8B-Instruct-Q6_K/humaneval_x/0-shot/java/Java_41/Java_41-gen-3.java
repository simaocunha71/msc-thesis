The problem is asking to find the number of collisions that will occur when two sets of n cars are moving in opposite directions on a straight road. The cars are infinitely sturdy and strong, so they will not stop or change direction after a collision.

To solve this problem, we can use the concept of a "meeting point". A meeting point is a point on the road where a car from the left-moving set and a car from the right-moving set will collide. We can find the number of meeting points by considering the left-moving cars and the right-moving cars separately.

For the left-moving cars, we can start from the leftmost car and consider each car one by one. For each car, we can find the distance it will travel before colliding with a car from the right-moving set. This distance is equal to the distance between the leftmost car and the car being considered.

For the right-moving cars, we can start from the rightmost car and consider each car one by one. For each car, we can find the distance it will travel before colliding with a car from the left-moving set. This distance is equal to the distance between the rightmost car and the car being considered.

The number of meeting points is equal to the minimum of the number of left-moving cars and the number of right-moving cars. This is because a car from the left-moving set can only collide with a car from the right-moving set at a meeting point.

Here is the Java code to solve this problem:

```java
public int carRaceCollision(int n) {
    int left = n;
    int right = n;
    int collisions = 0;
    while (left > 0 && right > 0) {
        if (left <= right) {
            left--;
            right--;
        } else {
            right--;
            left--;
        }
        collisions++;
    }
    return collisions;
}
```

In this code, we initialize the number of left-moving cars and right-moving cars to n. We then enter a loop that continues until both sets of cars have collided. In each iteration of the loop, we decrement the number of left-moving cars and right-moving cars by 1. We also increment the number of collisions by 1. The loop continues until both sets of cars have collided. The number of collisions is then returned.

This code has a time complexity of O(n) and a space complexity of O(1), where n is the number of cars. It is efficient and can handle large values of n.