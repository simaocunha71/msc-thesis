        Set<Integer> set = new HashSet<>();
        for (int num : l) {
            if (set.contains(-num)) return true;
            set.add(num);
        }
        return false;
    }
}

