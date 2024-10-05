        Set<Character> set = new HashSet<>();

        for (char c : s0.toCharArray()) {
            set.add(c);
        }

        for (char c : s1.toCharArray()) {
            if (!set.contains(c)) return false;
        }

        return true;
    }
}

