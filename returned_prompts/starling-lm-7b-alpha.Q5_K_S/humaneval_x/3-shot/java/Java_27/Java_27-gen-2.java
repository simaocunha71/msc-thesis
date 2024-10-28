        StringBuilder result = new StringBuilder();
        for (char c : string.toCharArray()) {
            if (c >= 'a' && c <= 'z') {
                result.append(Character.toUpperCase(c));
            } else if (c >= 'A' && c <= 'Z') {
                result.append(Character.toLowerCase(c));
            } else {
                result.append(c);
            }
        }
        return result.toString();
    }
}

