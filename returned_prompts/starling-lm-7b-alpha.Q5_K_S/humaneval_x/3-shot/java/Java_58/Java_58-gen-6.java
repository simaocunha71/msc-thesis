        Set<Integer> unique_common_set = new HashSet<>();
        for (int i : l1) {
            if (l2.contains(i)) {
                unique_common_set.add(i);
            }
        }
        List<Integer> result = new ArrayList<>(unique_common_set);
        Collections.sort(result);
        return result;
    }
}

