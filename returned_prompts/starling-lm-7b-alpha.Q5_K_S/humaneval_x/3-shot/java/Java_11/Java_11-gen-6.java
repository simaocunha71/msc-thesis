        char[] result = new char[a.length()];
        for (int i = 0; i < result.length; i++) {
            if (a.charAt(i) == '0' && b.charAt(i) == '0') {
                result[i] = '0';
            } else if (a.charAt(i) == '0' && b.charAt(i) == '1') {
                result[i] = '1';
            } else if (a.charAt(i) == '1' && b.charAt(i) == '0') {
                result[i] = '1';
            } else {
                result[i] = '0';
            }
        }
        return new String(result);
    }
}

