        String vowels = "aeiouAEIOU";
        StringBuilder result = new StringBuilder();

        for (char c : message.toCharArray()) {
            if (vowels.indexOf(c) >= 0) {
                result.append((char)((c - 'a' + 2) % 26 + 'a'));
            } else if (vowels.indexOf(Character.toUpperCase(c)) >= 0) {
                result.append((char)((c - 'A' + 2) % 26 + 'A'));
            } else {
                result.append(c);
            }
        }

        return result.toString();
    }
}

