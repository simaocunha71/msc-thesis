        StringBuilder result = new StringBuilder();

        for (int i = 0; i < Math.max(a.length(), b.length()); i++) {
            char a_digit = i < a.length() ? a.charAt(i) : '0';
            char b_digit = i < b.length() ? b.charAt(i) : '0';

            if (a_digit == '0' && b_digit == '0') {
                result.append('0');
            } else if (a_digit == '1' && b_digit == '1') {
                result.append('0');
            } else {
                result.append('1');
            }
        }
        return result.toString();
    }
}

