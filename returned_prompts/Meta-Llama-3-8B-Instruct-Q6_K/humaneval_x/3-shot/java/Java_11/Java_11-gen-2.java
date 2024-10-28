        StringBuilder result = new StringBuilder();
        for (int i = 0; i < a.length(); i++) {
            char c1 = a.charAt(i);
            char c2 = b.charAt(i);
            if (c1 == '1' && c2 == '1') {
                result.append('0');
            } else if (c1 == '0' && c2 == '0') {
                result.append('0');
            } else {
                result.append('1');
            }
        }
        return result.toString();

    }
}

