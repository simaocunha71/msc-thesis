        int result = 0;
        for (int i = 0; i < s.length(); i++) {
            char c = s.charAt(i);
            if (i % 2 == 0 && Character.isUpperCase(c)) {
                result += 1;
            }
        }
        return result;
    }
}

