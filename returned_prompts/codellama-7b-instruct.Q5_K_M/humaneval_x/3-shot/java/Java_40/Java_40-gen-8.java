        Set<Integer> set = new HashSet<>();
        for (int i : l) {
            set.add(i);
        }
        for (int i : set) {
            for (int j : set) {
                if (j + i == 0) return true;
            }
        }
        return false;
    }
}

