        StringBuilder result = new StringBuilder();
        for (int i = 0; i < a.length(); i++) {
            char ca = a.charAt(i);
            char cb = b.charAt(i);
            if (ca == '1' && cb == '1') {
                result.append('0');
            } else if (ca == '0' && cb == '0') {
                result.append('0');
            } else {
                result.append('1');
            }
        }
        return result.toString();
    }
}

