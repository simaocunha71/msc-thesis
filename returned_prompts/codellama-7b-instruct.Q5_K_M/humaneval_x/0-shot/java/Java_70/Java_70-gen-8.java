        if (lst.size() == 0) {
            return lst;
        }
        int min = lst.get(0);
        int max = lst.get(0);
        for (int i = 1; i < lst.size(); i++) {
            if (lst.get(i) < min) {
                min = lst.get(i);
            }
            if (lst.get(i) > max) {
                max = lst.get(i);
            }
        }
        lst.remove(max);
        lst.remove(min);
        lst.add(0, max);
        lst.add(0, min);
        return strangeSortList(lst);
    }
}
