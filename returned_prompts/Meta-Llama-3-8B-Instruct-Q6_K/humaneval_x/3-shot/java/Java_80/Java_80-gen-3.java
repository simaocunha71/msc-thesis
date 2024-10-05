        if (s.length() < 3) return false;
        for (int i = 0; i < s.length() - 2; i++) {
            if (s.substring(i, i + 3).chars().distinct().count() == 3) return true;
        }
        return false;
    }
}

