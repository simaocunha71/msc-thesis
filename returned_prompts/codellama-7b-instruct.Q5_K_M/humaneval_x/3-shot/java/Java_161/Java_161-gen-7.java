        StringBuilder result = new StringBuilder();
        boolean has_letter = false;

        for (char c : s.toCharArray()) {
            if (Character.isLetter(c)) {
                has_letter = true;
                result.append(Character.isUpperCase(c) ? Character.toLowerCase(c) : Character.toUpperCase(c));
            } else {
                result.append(c);
            }
        }
        return has_letter ? result.toString() : new StringBuilder(s).reverse().toString();
    }
}

