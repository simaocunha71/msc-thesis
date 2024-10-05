        StringBuilder result = new StringBuilder();
        boolean has_letter = false;
        for (char c : s.toCharArray()) {
            if (Character.isLetter(c)) {
                has_letter = true;
                if (Character.isLowerCase(c)) {
                    result.append(Character.toUpperCase(c));
                } else {
                    result.append(Character.toLowerCase(c));
                }
            } else {
                result.append(c);
            }
        }
        if (!has_letter) {
            result.reverse();
        }
        return result.toString();
    }
}

