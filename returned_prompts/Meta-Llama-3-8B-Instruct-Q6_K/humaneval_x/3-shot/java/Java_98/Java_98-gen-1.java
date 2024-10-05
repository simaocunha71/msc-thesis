        int count = 0;
        for (int i = 0; i < s.length(); i++) {
            if (i % 2 == 0 && isUpper(s.charAt(i))) {
                count++;
            }
        }
        return count;
    }

    private boolean isUpper(char c) {
        return Character.isUpperCase(c);
    }
}