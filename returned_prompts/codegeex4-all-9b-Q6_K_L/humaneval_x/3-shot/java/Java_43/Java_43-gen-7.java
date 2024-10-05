        Set<Integer> set = new HashSet<>();

        for (int n : l) {
            if (set.contains(-n)) return true;
            set.add(n);
        }
        return false;
    }
}

