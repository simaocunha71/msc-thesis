```java
public boolean cycpatternCheck(String a, String b) {
    if(b.length() > a.length()) {
        return false;
    }
    String temp = b;
    for(int i=0; i<b.length(); i++) {
        if(a.contains(temp)) {
            return true;
        }
        temp = temp.substring(1) + temp.charAt(0);
    }
    return false;
}
```
Explanation:

1. If the length of `b` is greater than `a`, it's impossible for `b` or any of its rotations to be a substring of `a`. So, we return `false`.

2. We create a temporary string `temp` and initialize it with `b`. Then, we iterate through each character of `b`. For each iteration, we check if `a` contains `temp`. If it does, we return `true`.

3. If `a` doesn't contain `temp`, we rotate `temp` by one character to the right by using the `substring` and `charAt` methods. This is equivalent to rotating `b` by one character to the right.

4. If we finish the iteration without finding `b` or any of its rotations in `a`, we return `false`.

This solution has a time complexity of O(n*m) where n is the length of `a` and m is the length of `b`. This is because in the worst case, we need to iterate through each character of `a` for each character of `b`. The space complexity is O(1) as we only use a constant amount of space to store the temporary string and the indices.