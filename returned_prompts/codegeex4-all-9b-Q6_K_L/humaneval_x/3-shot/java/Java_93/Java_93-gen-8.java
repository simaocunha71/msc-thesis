        StringBuilder result = new StringBuilder();
        for (char c : message.toCharArray()) {
            if (Character.isUpperCase(c)) {
                char new_char = Character.toLowerCase(c);
                if (new_char == 'a') new_char = 'c';
                if (new_char == 'e') new_char = 'g';
                if (new_char == 'i') new_char = 'k';
                if (new_char == 'o') new_char = 'q';
                if (new_char == 'u') new_char = 'w';
                result.append(new_char);
            } else {
                char new_char = Character.toUpperCase(c);
                if (new_char == 'a') new_char = 'c';
                if (new_char == 'e') new_char = 'g';
                if (new_char == 'i') new_char = 'k';
                if (new_char == 'o') new_char = 'q';
                if (new_char == 'u') new_char = 'w';
                result.append(new_char);
            }
        }
        return result.toString();
    }
}

