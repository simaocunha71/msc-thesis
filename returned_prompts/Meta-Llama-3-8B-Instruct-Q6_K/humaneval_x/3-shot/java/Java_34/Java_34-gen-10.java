        Set<Integer> set = new LinkedHashSet<Integer>();
        for (Integer i : l) {
            set.add(i);
        }
        List<Integer> list = new ArrayList<Integer>(set);
        Collections.sort(list);
        return list;
    }
}

