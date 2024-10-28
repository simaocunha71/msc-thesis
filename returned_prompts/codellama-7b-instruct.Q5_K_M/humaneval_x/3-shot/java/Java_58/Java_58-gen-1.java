        Set<Integer> result = new HashSet<>();
        for (int i : l1) {
            if (l2.contains(i)) {
                result.add(i);
            }
        }
        result.removeAll(Collections.singleton(null));
        result.removeAll(Collections.singleton(-1));
        result.removeAll(Collections.singleton(0));
        List<Integer> sorted_result = new ArrayList<>(result);
        Collections.sort(sorted_result);
        return sorted_result;
    }
}

