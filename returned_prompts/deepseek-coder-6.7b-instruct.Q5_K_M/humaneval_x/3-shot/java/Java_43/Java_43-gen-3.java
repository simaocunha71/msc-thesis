        Set<Integer> seen = new HashSet<>();
        for (int num : l) {
            if (seen.contains(-num)) {
                return true;
            }
            seen.add(num);
        }
        return false;
    }
}

