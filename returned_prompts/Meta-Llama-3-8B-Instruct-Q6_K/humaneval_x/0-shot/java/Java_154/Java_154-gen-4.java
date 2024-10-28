```java
public boolean cycpatternCheck(String a, String b) {
    String bRotations = b + b;
    return a.indexOf(b) != -1 || a.indexOf(bRotations) != -1;
}
```
Explanation:
This method checks if the second word or any of its rotations is a substring in the first word.
The rotation of the second word `b` is created by concatenating `b` with itself.
Then, it checks if `a` contains `b` or any of its rotations using the `indexOf` method.
If either of these conditions is true, the method returns `true`; otherwise, it returns `false`.