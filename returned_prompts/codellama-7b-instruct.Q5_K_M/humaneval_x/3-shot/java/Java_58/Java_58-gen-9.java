        Set<Integer> result = new HashSet<>();

        for (int i : l1) {
            for (int j : l2) {
                if (i == j) result.add(i);
            }
        }
        return new ArrayList<>(result);
    }
}

