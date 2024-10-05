```java
public boolean anyInt(Object x, Object y, Object z) {
        if (x instanceof Integer && y instanceof Integer && z instanceof Integer) {
            int a = (int) x;
            int b = (int) y;
            int c = (int) z;
            return (a + b == c || a + c == b || b + c == a);
        }
        return false;
    }
```
The function `anyInt` checks if all three objects are integers. If they are, it converts them to integers and checks if any of the numbers is equal to the sum of the other two. If any of these conditions are true, it returns `true`. Otherwise, it returns `false`.