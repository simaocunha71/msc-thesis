```java
public boolean rightAngleTriangle(int a, int b, int c) {
        // Sort the sides in ascending order
        int[] sides = {a, b, c};
        Arrays.sort(sides);
        
        // Check if the sum of the squares of the two smaller sides is equal to the square of the largest side
        return sides[0] * sides[0] + sides[1] * sides[1] == sides[2] * sides[2];
    }
```
The above code first sorts the sides in ascending order, then checks if the sum of the squares of the two smaller sides is equal to the square of the largest side, which is the definition of a right-angled triangle. If the condition is true, the function returns true, otherwise it returns false.