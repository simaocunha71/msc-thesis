        int result = 0;
        for (int i = 0; i < s.length(); i++) {
            if (i % 2 == 0) {
                if (s.charAt(i) >= 'A' && s.charAt(i) <= 'Z') {
                    result += 1;
                }
            }
        }
        return result;
    }
}

