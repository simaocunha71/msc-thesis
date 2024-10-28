        Set<Integer> result = new HashSet<>();
        for (int n : l1) {
            if (l2.contains(n)) result.add(n);
        }
        List<Integer> sorted = new ArrayList<>(result);
        Collections.sort(sorted);
        return sorted;
    }
}

