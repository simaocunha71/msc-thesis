        if (s.length() < 3) return false;

        for (int i = 0; i + 2 < s.length(); i++) {
            if (s.charAt(i) == s.charAt(i + 1) && s.charAt(i + 1) == s.charAt(i + 2)) return false;
        }
        return true;
    }
}

