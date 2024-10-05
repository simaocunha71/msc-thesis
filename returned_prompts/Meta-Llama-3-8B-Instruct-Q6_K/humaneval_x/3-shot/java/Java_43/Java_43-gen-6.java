        Set<Integer> seen = new HashSet<>();
        for (int x : l) {
            int complement = -x;
            if (seen.contains(complement)) {
                return true;
            }
            seen.add(x);
        }
        return false;
    }
}

