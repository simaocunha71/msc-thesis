```java
public int doubleTheDifference(List<Object> lst) {
    int result = 0;
    for (Object obj : lst) {
        if (obj instanceof Integer) {
            int num = (Integer) obj;
            if (num % 2 != 0) {
                result += num * num;
            }
        }
    }
    return result;
}
```