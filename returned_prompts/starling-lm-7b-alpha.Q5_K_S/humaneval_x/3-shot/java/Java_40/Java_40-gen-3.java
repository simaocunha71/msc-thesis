        Set<Integer> set = new HashSet<>(l);
        for (int i : l) {
            for (int j : l) {
                int k = -i - j;
                if (set.contains(k)) {
                    return true;
                }
            }
        }
        return false;
    }
}

