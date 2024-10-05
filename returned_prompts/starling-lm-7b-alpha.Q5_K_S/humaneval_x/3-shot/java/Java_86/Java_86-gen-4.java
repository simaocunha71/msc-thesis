        StringBuilder result = new StringBuilder();
        char[] chars = s.toCharArray();
        for (char c : chars) {
            if (c == ' ') {
                result.append(c);
            } else {
                result.append(getAscii(c));
            }
        }
        return result.toString();
    }

    private char getAscii(char c) {
        TreeSet<Character> chars = new TreeSet<>();
        chars.add(c);
        String chars_string = chars.toString();
        StringBuilder result = new StringBuilder();
        for (char ch : chars_string.toCharArray()) {
            result.append(ch);
        }
        return result.charAt(0);
    }
}


```