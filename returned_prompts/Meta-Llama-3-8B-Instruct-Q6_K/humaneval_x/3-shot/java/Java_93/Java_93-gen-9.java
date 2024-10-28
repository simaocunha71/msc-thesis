        StringBuilder result = new StringBuilder();
        for (char c : message.toCharArray()) {
            if (Character.isLetter(c)) {
                char base = Character.toLowerCase(c);
                if (base == 'a' || base == 'e' || base == 'i' || base == 'o' || base == 'u') {
                    base += 2;
                    if (base > 'u') base -= 26;
                } else {
                    base = Character.toUpperCase(base);
                }
                result.append(base);
            } else {
                result.append(c);
            }
        }
        return result.toString();
    }
}

