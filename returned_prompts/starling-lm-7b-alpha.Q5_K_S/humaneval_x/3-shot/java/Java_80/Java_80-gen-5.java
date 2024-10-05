        if (s.length() < 3) return false;

        Set<String> seen = new HashSet<>();
        for (int i = 0; i < s.length() - 2; i++) {
            String sub_s = s.substring(i, i + 3);
            if (seen.contains(sub_s)) return false;
            seen.add(sub_s);
        }
        return true;
    }
}

