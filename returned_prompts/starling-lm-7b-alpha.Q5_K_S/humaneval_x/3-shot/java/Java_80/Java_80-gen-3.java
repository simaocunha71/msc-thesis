        if (s.length() < 3) return false;
        Set<Character> set = new HashSet<>();
        for (int i = 0; i < 3; i++) {
            set.add(s.charAt(i));
        }
        for (int i = 3; i < s.length(); i++) {
            if (set.contains(s.charAt(i))) return false;
            set.add(s.charAt(i));
        }
        return true;
    }
}

