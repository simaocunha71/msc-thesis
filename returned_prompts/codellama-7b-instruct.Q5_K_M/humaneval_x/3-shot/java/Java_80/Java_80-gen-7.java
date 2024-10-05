        if (s.length() < 3) return false;

        for (int i = 0; i <= s.length() - 3; i++) {
            if (s.charAt(i) == s.charAt(i + 1) && s.charAt(i) == s.charAt(i + 2)) {
                return false;
            }
        }
        return true;
    }
}

