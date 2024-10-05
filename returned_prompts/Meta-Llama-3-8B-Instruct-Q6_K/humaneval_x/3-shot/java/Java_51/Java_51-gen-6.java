        StringBuilder result = new StringBuilder();
        for (char c : text.toCharArray()) {
            if (c == 'a' || c == 'e' || c == 'i' || c == 'o' || c == 'u' || c == 'A' || c == 'E' || c == 'I' || c == 'O' || c == 'U') {
                continue;
            }
            result.append(c);
        }
        return result.toString();
    }
}

