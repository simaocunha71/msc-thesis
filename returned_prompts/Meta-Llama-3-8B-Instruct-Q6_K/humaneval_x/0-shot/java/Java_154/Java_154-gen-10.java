```java
public boolean cycpatternCheck(String a, String b) {
    if(b.length() > a.length()) return false;
    for(int i = 0; i < a.length(); i++) {
        String temp = a.substring(i) + a.substring(0, i);
        if(temp.contains(b)) return true;
    }
    return false;
}
```
Explanation:
This problem is asking whether the second word or any of its rotations is a substring in the first word. The approach here is to generate all possible rotations of the first word and then check if the second word is a substring of any of these rotations. 

The function `cycpatternCheck` takes two parameters `a` and `b`, where `a` is the first word and `b` is the second word. It first checks if `b` is longer than `a`. If it is, it immediately returns `false` because `b` cannot be a substring of `a` if it is longer.

Then it enters a loop where it generates all possible rotations of `a` by taking a substring of `a` from the current index to the end, and concatenating it with the substring of `a` from the start to the current index. This effectively rotates the word `a` by one position.

Inside the loop, it checks if the second word `b` is a substring of the current rotation of `a`. If it is, it immediately returns `true` because it has found a rotation of `a` that contains `b`.

If the loop completes without finding a rotation of `a` that contains `b`, it returns `false` because `b` is not a substring of `a` or any of its rotations. 

This approach has a time complexity of O(n*m) where n is the length of `a` and m is the length of `b`, because in the worst case it needs to generate all possible rotations of `a` and check if `b` is a substring of each rotation. The space complexity is O(1) because it only uses a constant amount of space to store the temporary rotation of `a`. 