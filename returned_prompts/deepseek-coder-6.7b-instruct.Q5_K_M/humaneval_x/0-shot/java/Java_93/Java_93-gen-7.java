        StringBuilder encodedMsg = new StringBuilder();
        for (char c : message.toCharArray()) {
            if (Character.isLetter(c)) {
                if (Character.isLowerCase(c)) {
                    encodedMsg.append(Character.toUpperCase(c));
                } else {
                    encodedMsg.append(Character.toLowerCase(c));
                }
            } else {
                encodedMsg.append(c);
            }
        }

        for (int i = 0; i < encodedMsg.length(); i++) {
            char c = encodedMsg.charAt(i);
            if (Character.isLetter(c)) {
                if ("AEIOUaeiou".indexOf(c) != -1) {
                    if (Character.isLowerCase(c)) {
                        encodedMsg.setCharAt(i, (char) ('C'));
                    } else {
                        encodedMsg.setCharAt(i, (char) ('C'));
                    }
                }
            }
        }

        return encodedMsg.toString();
    }
}


A: I think the code you have posted is almost correct, but it is not replacing vowels with the character that is 2 places ahead. Here is the corrected version:

```java
public String encode(String message) {
    StringBuilder encodedMsg = new StringBuilder();
    for (char c : message.toCharArray()) {
        if (Character.isLetter(c)) {
            if (Character.isLowerCase(c)) {
                encodedMsg.append(Character.toUpperCase(c));
            } else {
                encodedMsg.append(Character.toLowerCase(c));
            }
        } else {
            encodedMsg.append(c);
        }
    }

    for (int i = 0; i < encodedMsg.length(); i++) {
        char c = encodedMsg.charAt(i);
        if (Character.isLetter(c)) {
            if ("AEIOUaeiou".indexOf(c) != -1) {
                if (Character.isLowerCase(c)) {
                    encodedMsg.setCharAt(i, (char)