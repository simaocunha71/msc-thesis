        Set<Integer> seen = new HashSet<>();
        for (int x : l) {
            if (seen.contains(-x)) return true;
            seen.add(x);
        }
        return false;
    }
}

