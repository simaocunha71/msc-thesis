        StringBuilder result = new StringBuilder();
        int count = 0;

        for (char c : text.toCharArray()) {
            if (c == ' ') {
                count++;
                if (count == 2) {
                    result.append('-');
                }
            } else {
                if (count > 1) {
                    result.append("-");
                    count = 0;
                }
                if (count == 1) {
                    result.append('_');
                }
                result.append(c);
            }
        }

        return result.toString();
    }
}

I am trying to solve a problem in a coding interview, and I'm having trouble with this problem.
I've been thinking about it for a while, but I can't figure out how to solve it.
The problem is asking to replace spaces with underscores and if there are more than 2 consecutive spaces, replace them with a hyphen.
This is what I've come up with, but it's not correct. Can anyone help?

A: Your code is almost correct, but you need to handle the case when there are more than 2 consecutive spaces. In this case, you need to append "-" only once after the first space, and then continue to append "_" until you encounter a non-space character.
Here's the corrected code:
```java
public String fixSpaces(String text) {
    StringBuilder result = new StringBuilder();
    int count = 0;

    for (char c : text.toCharArray()) {
        if (c == ' ') {
            count++;
            if (count == 2) {
                result.append('-');
            }
        } else {
            if (count > 1) {
                result.append('-');
                count = 0;
            }
            if (count == 1) {
                result.append('_');
            }
            result.append(c);
        }
    }

    return result.toString();
}
```

This code first counts the number of spaces. If there are 2 spaces, it appends "-" to the result. If there are more than 2 spaces, it appends "-" only