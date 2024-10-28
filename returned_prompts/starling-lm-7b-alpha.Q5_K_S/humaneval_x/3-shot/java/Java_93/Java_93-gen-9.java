        StringBuilder result = new StringBuilder();
        for (int i = 0; i < message.length(); i++) {
            char c = message.charAt(i);
            if (c >= 'A' && c <= 'Z') {
                result.append((char) (c + ('z' - 'a')));
            } else if (c >= 'a' && c <= 'z') {
                result.append((char) (c - ('z' - 'a')));
            } else if (c == ' ') {
                result.append(c);
            } else {
                result.append((char) (c + ('a' - 'A')));
            }
        }
        return result.toString();
    }
}


class MyClass {
    public static void main(String args[]) {
        Solution solution = new Solution();
        solution.encode("This is a message");
        System.out.println("Hello, World!");
    }
}

```