        Set<Integer> result = new HashSet<>();
        for (int i : l1) {
            if (l2.contains(i)) result.add(i);
        }
        List<Integer> list = new ArrayList<>(result);
        Collections.sort(list);
        return list;
    }
}

