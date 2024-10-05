```java
public int digitSum(String s) {
    int sum = 0;
    for (char c : s.toCharArray()) {
        if (Character.isUpperCase(c)) {
            sum += c;
        }
    }
    return sum;
}
```
Explanation:
The function iterates over each character in the input string. If the character is an uppercase letter, it adds the ASCII value of that character to the sum. The ASCII value of an uppercase letter is its position in the alphabet (A=65, B=66, ..., Z=90). The sum of these ASCII values is returned as the result. If the input string contains lowercase letters or digits, they are ignored since the problem only asks for the sum of upper characters' ASCII codes.