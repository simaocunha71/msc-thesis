        StringBuilder result = new StringBuilder();
        for (char c : message.toCharArray()) {
            if (Character.isLetter(c)) {
                char new_c = Character.toLowerCase(c);
                if ("aeiou".indexOf(new_c) != -1) {
                    new_c = (char) (new_c + 2);
                }
                result.append(new_c);
            } else {
                result.append(c);
            }
        }
        return result.toString();
    }
}

