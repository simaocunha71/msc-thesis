        Set<Integer> seen = new HashSet<>();
        for (int x : l) {
            for (int y : l) {
                int complement = -x - y;
                if (seen.contains(complement)) {
                    return true;
                }
                seen.add(y);
            }
            seen.clear();
        }
        return false;
    }
}

