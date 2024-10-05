        StringBuilder result = new StringBuilder();
        for (char c : message.toCharArray()) {
            char upper = Character.toUpperCase(c);
            if (upper >= 'A' && upper <= 'Z') {
                if (upper == 'A') result.append('a');
                else if (upper == 'E') result.append('g');
                else if (upper == 'I') result.append('k');
                else if (upper == 'O') result.append('q');
                else if (upper == 'U') result.append('w');
                else result.append(Character.toLowerCase(c));
            } else {
                result.append(c);
            }
        }
        return result.toString();
    }
}

