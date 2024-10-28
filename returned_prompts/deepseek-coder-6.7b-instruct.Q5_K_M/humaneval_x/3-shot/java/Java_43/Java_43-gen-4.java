        Set<Integer> set = new HashSet<>(l);

        for (int num : l) {
            if (set.contains(-num)) {
                return true;
            }
        }

        return false;
    }
}

