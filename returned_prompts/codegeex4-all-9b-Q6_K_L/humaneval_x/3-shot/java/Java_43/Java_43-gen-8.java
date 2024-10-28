        Set<Integer> set = new HashSet<>();
        for (int i : l) {
            if (set.contains(-i)) {
                return true;
            } else {
                set.add(i);
            }
        }
        return false;
    }
}

