        if (s.length() < 3) return false;

        for (int i = 0; i < s.length() - 2; i++) {
            if (s.substring(i, i + 3).equals(s.substring(i + 1, i + 4))) return false;
        }
        return true;
    }
}

