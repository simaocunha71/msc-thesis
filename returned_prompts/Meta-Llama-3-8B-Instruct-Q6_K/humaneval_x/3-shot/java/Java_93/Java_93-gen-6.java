        StringBuilder result = new StringBuilder();
        for (char c : message.toCharArray()) {
            if (Character.isLetter(c)) {
                char original_case = Character.isUpperCase(c) ? 'U' : 'L';
                char new_case = original_case == 'U' ? 'L' : 'U';
                char new_char = (char) (c + (c >= 'a' && c <= 'z') ? 2 : -2);
                result.append(new_case).append(new_char);
            } else {
                result.append(c);
            }
        }
        return result.toString();
    }
}

