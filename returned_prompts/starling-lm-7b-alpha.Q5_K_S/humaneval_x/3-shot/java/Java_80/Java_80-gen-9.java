        if (s.length() < 3) return false;
        Set<Character> letters = new HashSet<>();
        for (int i = 0; i < 3; i++) {
            if (!letters.add(s.charAt(i))) return false;
        }
        return true;
    }
}

