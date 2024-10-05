Here is a Java function that checks if the object `q` will fly:

```java
public boolean willItFly(List<Integer> q, int w) {
    int sum = 0;
    StringBuilder sb = new StringBuilder();
    for (int num : q) {
        sum += num;
        sb.append(num);
        if (!sb.toString().equals(sb.reverse().toString())) {
            return false;
        }
    }
    return sum <= w;
}
```

This function calculates the sum of the elements in the list and checks if the list is a palindrome. If the list is not a palindrome, the function returns `false`. If the list is a palindrome, the function checks if the sum is less than or equal to the maximum possible weight `w`. If the sum is less than or equal to `w`, the function returns `true`. Otherwise, it returns `false`. 