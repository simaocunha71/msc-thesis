        if (s.length() < 3) return false;
        if (s.length() % 3 == 0) {
            int count = 0;
            for (int i = 0; i < s.length() - 2; i += 3) {
                if (s.charAt(i) == s.charAt(i + 1) && s.charAt(i + 1) == s.charAt(i + 2)) {
                    count += 1;
                }
            }
            if (count != 0) return false;
        }
        return true;
    }
}

