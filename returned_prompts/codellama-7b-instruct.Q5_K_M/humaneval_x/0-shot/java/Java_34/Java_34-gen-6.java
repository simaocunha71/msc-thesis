        Collections.sort(l);
        List<Integer> uniq = new ArrayList<Integer>();
        for (Integer i : l) {
            if (i == l.get(0)) {
                uniq.add(i);
            } else {
                if (i != l.get(l.size() - 1)) {
                    if (i != uniq.get(uniq.size() - 1)) {
                        uniq.add(i);
                    }
                }
            }
        }
        return uniq;
    }
}
