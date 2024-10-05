        int result = 0;
        for (int i = 0; i < s.length(); i++) {
            if (i % 2 == 0 && "AEIOU".contains(s.substring(i, i + 1).toUpperCase())) {
                result += 1;
            }
        }
        return result;
    }
}

