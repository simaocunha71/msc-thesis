        Set<Integer> result = new HashSet<>();
        Set<Integer> l1_set = new HashSet<>(l1);
        for (Integer i : l2) {
            if (l1_set.contains(i)) result.add(i);
        }
        List<Integer> result_list = new ArrayList<>(result);
        Collections.sort(result_list);
        return result_list;
    }
}

