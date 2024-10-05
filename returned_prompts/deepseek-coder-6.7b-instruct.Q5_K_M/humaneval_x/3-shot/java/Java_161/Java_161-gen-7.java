        StringBuilder result = new StringBuilder();
        boolean hasLetters = false;
        for (char c : s.toCharArray()) {
            if (Character.isLetter(c)) {
                hasLetters = true;
                if (Character.isUpperCase(c)) {
                    result.append(Character.toLowerCase(c));
                } else {
                    result.append(Character.toUpperCase(c));
                }
            } else {
                result.append(c);
            }
        }
        if (!hasLetters) {
            result.reverse();
        }
        return result.toString();
     }
}

