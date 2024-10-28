```java
public boolean iscube(int a) {
    if(a < 0) {
        a = -a;
    }
    int root = (int) Math.pow(a, 1.0/3.0);
    return Math.pow(root, 3) == a;
}
```