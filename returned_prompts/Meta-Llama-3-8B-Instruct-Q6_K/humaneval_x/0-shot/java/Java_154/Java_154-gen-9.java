Here is the solution in Java:
```java
public boolean cycpatternCheck(String a, String b) {
    if (a == null || b == null) {
        return false;
    }
    int lenA = a.length();
    int lenB = b.length();
    if (lenB > lenA) {
        return false;
    }
    for (int i = 0; i < lenA - lenB + 1; i++) {
        if (a.substring(i, i + lenB).equals(b)) {
            return true;
        }
    }
    for (int i = 0; i < lenB; i++) {
        String rotatedB = b.substring(i) + b.substring(0, i);
        if (a.contains(rotatedB)) {
            return true;
        }
    }
    return false;
}
```
The idea is to check if the second word or any of its rotations is a substring in the first word. We first check if the second word is a substring of the first word. If it's not, then we rotate the second word by one character at a time and check if the rotated word is a substring of the first word. If we find a match, we return true. If we don't find a match after checking all rotations, we return false. 

The time complexity of this solution is O(n), where n is the length of the first word. The space complexity is O(1), as we are not using any extra space that scales with the input size. 