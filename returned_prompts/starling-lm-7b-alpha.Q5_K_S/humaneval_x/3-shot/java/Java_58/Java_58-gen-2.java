        List<Integer> result = new ArrayList<>();
        Set<Integer> l1_set = new HashSet<>(l1);
        for (int n : l2) {
            if (l1_set.contains(n)) {
                result.add(n);
                l1_set.remove(n);
            }
        }
        return result;
    }
}

