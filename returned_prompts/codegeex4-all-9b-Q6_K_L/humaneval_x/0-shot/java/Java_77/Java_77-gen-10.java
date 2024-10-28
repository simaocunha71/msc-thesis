```java
public boolean iscube(int a) {
        if(a < 0) {
            a *= -1;
        }
        int root = (int) Math.round(Math.pow(a, 1.0/3.0));
        return root*root*root == a;
    }
```