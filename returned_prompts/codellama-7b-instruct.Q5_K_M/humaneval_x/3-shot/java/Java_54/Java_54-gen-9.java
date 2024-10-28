        if (s0.length() != s1.length()) return false;

        Set<Character> chars0 = new HashSet<>();
        for (char c : s0.toCharArray()) chars0.add(c);

        for (char c : s1.toCharArray()) {
            if (!chars0.contains(c)) return false;
        }
        return true;
    }
}

