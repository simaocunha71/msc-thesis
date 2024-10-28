        Set<Integer> set = new HashSet<>();
        set.addAll(l);
        List<Integer> list = new ArrayList<>(set);
        Collections.sort(list);
        return list;
    }
}

