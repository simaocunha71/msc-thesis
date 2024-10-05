        if (s.length() < 3) return false;
        for (int i = 0; i < s.length() - 2; i++) {
            String three_chars = s.substring(i, i + 3);
            if (three_chars.length() != 3 || three_chars.indexOf(three_chars.charAt(0)) != 0) return false;
        }
        return true;
    }
}

