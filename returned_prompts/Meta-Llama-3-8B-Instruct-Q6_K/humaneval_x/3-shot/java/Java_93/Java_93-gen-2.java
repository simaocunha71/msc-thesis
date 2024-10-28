        StringBuilder result = new StringBuilder();
        for (char c : message.toCharArray()) {
            if (Character.isLetter(c)) {
                char base = Character.isUpperCase(c) ? 'A' : 'a';
                c = (char) ((c - base + (Character.isUpperCase(c) ? 2 : -2)) % 26 + base);
                c = Character.toUpperCase(c);
            }
            result.append(c);
        }
        return result.toString();
    }
}

