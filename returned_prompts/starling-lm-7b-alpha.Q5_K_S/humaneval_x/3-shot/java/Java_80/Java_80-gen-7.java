        if (s.length() < 3) return false;
        Set<String> set = new HashSet<>();
        for (int i = 0; i < s.length() - 2; i++) {
            if (set.contains(s.substring(i, i + 3))) return false;
            set.add(s.substring(i, i + 3));
        }
        return true;
    }
}

