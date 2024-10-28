        if (s.length() < 3) {
            return false;
        }
        for (int i = 0; i < s.length() - 2; i++) {
            String substring = s.substring(i, i + 3);
            if (substring.length() != 3 || hasDuplicates(substring)) {
                return false;
            }
        }
        return true;
    }

    private boolean hasDuplicates(String s) {
        Set<Character> set = new HashSet<>();
        for (char c : s.toCharArray()) {
            if (!set.add(c)) {
                return true;
            }
        }
        return false;
    }
}

