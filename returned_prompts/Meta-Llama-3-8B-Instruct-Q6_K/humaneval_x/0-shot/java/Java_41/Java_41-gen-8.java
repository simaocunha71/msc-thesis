The problem is asking to find the number of collisions that will occur in a road where n cars are moving left to right and n cars are moving right to left. The cars are infinitely sturdy and strong, so they will not stop or change direction even if they collide. We need to find the number of pairs of cars that will collide.

One way to solve this problem is to use a priority queue. We can add all the cars moving left to right to the priority queue and then add all the cars moving right to left. Then, we can pop the cars from the priority queue and check if the popped car collides with any of the cars that are still in the queue. If a collision is found, we increment the collision count.

Here is the Java code for the solution:

```java
import java.util.*;

class Solution {
    public int carRaceCollision(int n) {
        PriorityQueue<Integer> left = new PriorityQueue<>();
        PriorityQueue<Integer> right = new PriorityQueue<>();

        for (int i = 1; i <= n; i++) {
            left.add(i);
        }
        for (int i = n; i >= 1; i--) {
            right.add(i);
        }

        int collisionCount = 0;
        while (!left.isEmpty() && !right.isEmpty()) {
            int leftCar = left.poll();
            int rightCar = right.peek();
            if (leftCar >= rightCar) {
                collisionCount++;
                left.add(leftCar);
            } else {
                left.add(leftCar);
                right.poll();
            }
        }

        return collisionCount;
    }
}
```

In this code, we first create two priority queues, one for the cars moving left to right and one for the cars moving right to left. Then, we pop the cars from the priority queues and check for collisions. If a collision is found, we increment the collision count and add the car back to the left queue. If no collision is found, we add the car back to the left queue and remove the car from the right queue. We continue this process until one of the queues is empty. The collision count is the number of collisions that occurred. This solution has a time complexity of O(n log n) due to the use of priority queues.