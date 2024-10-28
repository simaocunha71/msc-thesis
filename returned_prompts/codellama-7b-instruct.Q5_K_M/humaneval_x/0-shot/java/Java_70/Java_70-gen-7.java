        List<Integer> result = new ArrayList<Integer>();
        if (lst.size() == 0) return result;
        Collections.sort(lst);
        int min = lst.get(0);
        result.add(min);
        lst.remove(0);
        for (int i = 0; i < lst.size(); i++) {
            if (lst.get(i) > min) {
                result.add(lst.get(i));
                lst.remove(i);
                i = -1;
            }
        }
        for (int i = 0; i < lst.size(); i++) {
            if (lst.get(i) < min) {
                result.add(lst.get(i));
                lst.remove(i);
                i = -1;
            }
        }
        result.add(min);
        return result;
    }
}

