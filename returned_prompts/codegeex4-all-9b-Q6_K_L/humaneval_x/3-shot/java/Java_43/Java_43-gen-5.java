        Set<Integer> set = new HashSet<>();

        for (int x : l) {
            if (set.contains(-x)) return true;
            set.add(x);
        }
        return false;
    }
}

