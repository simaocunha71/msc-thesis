        if (s.length() < 3) return false;

        Set<String> distinct_chars = new HashSet<>();
        for (int i = 0; i < s.length() - 2; i++) {
            String substring = s.substring(i, i + 3);
            if (!distinct_chars.add(substring)) return false;
        }
        return true;
    }
}

