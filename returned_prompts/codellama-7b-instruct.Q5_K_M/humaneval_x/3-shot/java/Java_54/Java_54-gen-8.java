        Set<Character> s0_set = new HashSet<>();
        for (char c : s0.toCharArray()) s0_set.add(c);

        Set<Character> s1_set = new HashSet<>();
        for (char c : s1.toCharArray()) s1_set.add(c);

        return s0_set.equals(s1_set);
    }
}

