        int count = 0;
        for (char c : s.toCharArray()) {
            if (c == 'a' || c == 'e' || c == 'i' || c == 'o' || c == 'u' || c == 'A' || c == 'E' || c == 'I' || c == 'O' || c == 'U') {
                count += 1;
            }
        }
        if (s.length() > 0 && (s.charAt(s.length() - 1) == 'y' || s.charAt(s.length() - 1) == 'Y')) {
            count += 1;
        }
        return count;
    }
}

