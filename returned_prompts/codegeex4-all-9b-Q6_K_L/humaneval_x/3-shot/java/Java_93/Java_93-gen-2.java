        StringBuilder result = new StringBuilder();
        for (char c : message.toCharArray()) {
            if (Character.isLetter(c)) {
                char new_c = Character.isLowerCase(c) ? Character.toUpperCase(c) : Character.toLowerCase(c);
                if (new_c == 'a') {
                    result.append('c');
                } else if (new_c == 'e') {
                    result.append('g');
                } else if (new_c == 'i') {
                    result.append('k');
                } else if (new_c == 'o') {
                    result.append('q');
                } else if (new_c == 'u') {
                    result.append('w');
                } else {
                    result.append(new_c);
                }
            } else {
                result.append(c);
            }
        }
        return result.toString();
    }
}

