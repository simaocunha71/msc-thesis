        Set<Integer> seen = new HashSet<>();
        for (int n : l) {
            if (seen.contains(-n)) {
                return true;
            }
            seen.add(n);
        }
        return false;
    }
}

