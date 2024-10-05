        StringBuilder result = new StringBuilder();
        for (int i = 0; i < a.length(); i++) {
            char a_char = a.charAt(i);
            char b_char = b.charAt(i);
            if (a_char == '0' && b_char == '0') {
                result.append('0');
            } else if (a_char == '0' && b_char == '1') {
                result.append('1');
            } else if (a_char == '1' && b_char == '0') {
                result.append('1');
            } else {
                result.append('0');
            }
        }
        return result.toString();
    }
}

