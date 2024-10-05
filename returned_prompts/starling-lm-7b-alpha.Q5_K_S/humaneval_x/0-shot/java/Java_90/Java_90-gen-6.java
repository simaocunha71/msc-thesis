        List<Integer> ls = new ArrayList<>();
        for (int i = 0; i < lst.size(); i++) {
            if (i == 0 && lst.get(i) > lst.get(i + 1)) {
                ls.add(lst.get(i + 1));
                continue;
            }
            if (i == lst.size() - 1 && lst.get(i) > lst.get(i - 1)) {
                ls.add(lst.get(i));
                continue;
            }
            if (lst.get(i) > lst.get(i + 1) && lst.get(i) > lst.get(i - 1)) {
                ls.add(lst.get(i));
                continue;
            }
            if (lst.get(i) > lst.get(i + 1) || lst.get(i) > lst.get(i - 1)) {
                ls.add(lst.get(i));
            }
        }
        if (ls.size() < 2) {
            return Optional.empty();
        }
        Collections.sort(ls);
        return Optional.of(ls.get(1));

    }
}





































































































































































































