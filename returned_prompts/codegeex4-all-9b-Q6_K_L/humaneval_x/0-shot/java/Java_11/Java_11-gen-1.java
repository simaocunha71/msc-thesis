public String stringXor(String a, String b) {
    StringBuilder sb = new StringBuilder();
    for (int i = 0; i < a.length(); i++) {
        if (a.charAt(i) != b.charAt(i)) {
            sb.append('1');
        } else {
            sb.append('0');
        }
    }
    return sb.toString();
}

Explanation:
The function takes two strings `a` and `b` as input and returns the result of their binary XOR operation as a string.

The function first creates a `StringBuilder` object `sb` to store the result.

Then, it iterates through each character of the strings `a` and `b` using a for loop. For each character, it checks if the characters at the same position in the strings are different. If they are, it appends '1' to the `StringBuilder` object `sb`. Otherwise, it appends '0'.

Finally, it returns the result by converting the `StringBuilder` object `sb` to a string using the `toString()` method.