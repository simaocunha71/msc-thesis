        StringBuilder result = new StringBuilder();
        for (char c : message.toCharArray()) {
            if (Character.isLetter(c)) {
                if (Character.isLowerCase(c)) {
                    result.append(Character.toUpperCase(c));
                } else {
                    result.append(Character.toLowerCase(c));
                }
            } else {
                result.append(c);
            }

            if (Character.toString(c).matches("[aeiouAEIOU]")) {
                if (Character.isLowerCase(c)) {
                    result.append(Character.toString((char) (c + 2)));
                } else {
                    result.append(Character.toString((char) (c + 2)).toUpperCase());
                }
            }
        }
        return result.toString();
    }
}

