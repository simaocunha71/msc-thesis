        if (l.size() < 3) return false;
        Set<Integer> distinct = new HashSet<>();
        for (int i : l) {
            if (distinct.contains(i)) continue;
            distinct.add(i);
            for (int j : l) {
                if (i == j) continue;
                for (int k : l) {
                    if (i == k || j == k) continue;
                    if (i + j + k == 0) return true;
                }
            }
        }
        return false;
    }
}

