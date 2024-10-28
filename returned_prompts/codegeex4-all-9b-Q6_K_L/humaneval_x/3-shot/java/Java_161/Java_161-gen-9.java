        StringBuilder result = new StringBuilder();
        boolean has_letter = false;

        for (char c : s.toCharArray()) {
            if (Character.isLetter(c)) {
                result.append(Character.isUpperCase(c) ? Character.toLowerCase(c) : Character.toUpperCase(c));
                has_letter = true;
            } else {
                result.append(c);
            }
        }

        if (!has_letter) {
            return result.reverse().toString();
        } else {
            return result.toString();
        }
    }
}

