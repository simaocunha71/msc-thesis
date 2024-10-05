        if (s.length() < 3) return false;
        Set<Character> set = new HashSet<>();
        for (int i = 0; i < 3; i++) {
            if (!set.add(s.charAt(i))) return false;
        }
        return true;
    }
}

