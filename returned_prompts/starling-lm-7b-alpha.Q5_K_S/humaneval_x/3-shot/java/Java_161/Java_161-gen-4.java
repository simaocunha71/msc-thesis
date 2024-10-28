        StringBuilder result = new StringBuilder();
        for (int i = 0; i < s.length(); i++) {
            if (Character.isLetter(s.charAt(i))) {
                result.append(Character.isLowerCase(s.charAt(i)) ? Character.toUpperCase(s.charAt(i)) : Character.toLowerCase(s.charAt(i)));
            } else {
                result.append(s.charAt(i));
            }
        }
        return result.toString();
    }
}

