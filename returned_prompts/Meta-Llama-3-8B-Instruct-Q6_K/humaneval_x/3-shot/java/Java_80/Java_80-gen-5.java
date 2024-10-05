        if (s.length() < 3) return false;
        for (int i = 0; i < s.length() - 2; i++) {
            for (int j = i + 1; j < s.length() - 1; j++) {
                for (int k = j + 1; k < s.length(); k++) {
                    if (s.charAt(i) == s.charAt(j) || s.charAt(j) == s.charAt(k) || s.charAt(i) == s.charAt(k)) return false;
                }
            }
        }
        return true;
    }
}

