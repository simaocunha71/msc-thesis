```java
public int fizzBuzz(int n) {
    int count = 0;
    for (int i = 1; i < n; i++) {
        if (i % 11 == 0 || i % 13 == 0) {
            String str = String.valueOf(i);
            for (int j = 0; j < str.length(); j++) {
                if (str.charAt(j) == '7') {
                    count++;
                }
            }
        }
    }
    return count;
}
```