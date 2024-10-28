        StringBuilder result = new StringBuilder();
        boolean hasLetter = false;

        for (char c : s.toCharArray()) {
            if (Character.isLetter(c)) {
                hasLetter = true;
                if (Character.isUpperCase(c)) {
                    result.append(Character.toLowerCase(c));
                } else {
                    result.append(Character.toUpperCase(c));
                }
            } else {
                result.append(c);
            }
        }
        if (!hasLetter) {
            return result.reverse().toString();
        }
        return result.toString();
    }
}

