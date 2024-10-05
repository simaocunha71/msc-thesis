        StringBuilder result = new StringBuilder();

        for(int i = 0; i < a.length(); i++) {
            if(a.charAt(i) == b.charAt(i)) {
                result.append('0');
            } else {
                result.append('1');
            }
        }

        return result.toString();
    }
}

The above solution is correct. It creates a StringBuilder object to store the result. The for loop iterates through each character in the strings. If the characters at the same index are equal, it appends '0' to the result, else it appends '1'. Finally, it returns the result as a string.

I am sorry, but I think there might be a misunderstanding in your question. In the question, it says that the inputs are two binary strings, but the code is written to handle binary strings. If you want to perform XOR operation on two binary strings, then you can simply use the bitwise XOR operator '^' in Java. Here is the corrected code:

```java
public String stringXor(String a, String b) {
    StringBuilder result = new StringBuilder();

    for(int i = 0; i < a.length(); i++) {
        char xor = (char)((a.charAt(i) - '0') ^ (b.charAt(i) - '0') + '0');
        result.append(xor);
    }

    return result.toString();
}
```

This code converts the characters to their integer equivalents using the charAt method and subtracting '0' from them to get the actual integer values. Then it performs the XOR operation on these integers and converts the result back to a character by adding '0' to it. This result is then appended to the StringBuilder