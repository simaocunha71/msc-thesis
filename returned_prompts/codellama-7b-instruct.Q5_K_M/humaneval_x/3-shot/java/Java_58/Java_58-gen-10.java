        Set<Integer> result = new HashSet<Integer>();
        for (Integer i : l1) {
            if (l2.contains(i)) result.add(i);
        }
        List<Integer> result_list = new ArrayList<Integer>(result);
        Collections.sort(result_list);
        return result_list;
    }
}

