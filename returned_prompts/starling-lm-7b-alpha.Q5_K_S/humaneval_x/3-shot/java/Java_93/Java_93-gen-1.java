        StringBuilder result = new StringBuilder();
        for (char c : message.toCharArray()) {
            if (c >= 'a' && c <= 'z') {
                result.append(Character.toLowerCase((char) (c - 'a' + 'A')));
            } else if (c >= 'A' && c <= 'Z') {
                result.append(Character.toLowerCase((char) (c - 'A' + 'a')));
            } else {
                char next = (char) (c - 2);
                if (next < 'a') next = 'z';
                result.append(next);
            }
        }
        return result.toString();
    }
}

