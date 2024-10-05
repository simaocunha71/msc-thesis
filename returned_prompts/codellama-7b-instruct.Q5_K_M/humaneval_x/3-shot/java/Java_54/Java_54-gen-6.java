        HashSet<Character> hashSet = new HashSet<>();

        for (char c : s0.toCharArray()) {
            hashSet.add(c);
        }

        for (char c : s1.toCharArray()) {
            if (!hashSet.contains(c)) return false;
        }
        return true;
    }
}

