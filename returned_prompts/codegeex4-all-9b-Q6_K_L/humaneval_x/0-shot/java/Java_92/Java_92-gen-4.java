```java
public boolean anyInt(Object x, Object y, Object z) {
  if (x instanceof Integer && y instanceof Integer && z instanceof Integer) {
    int a = (int)x;
    int b = (int)y;
    int c = (int)z;
    return a == b + c || b == a + c || c == a + b;
  }
  return false;
}
```
