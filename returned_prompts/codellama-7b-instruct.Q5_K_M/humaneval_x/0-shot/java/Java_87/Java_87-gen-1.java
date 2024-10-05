        List<List<Integer>> res = new ArrayList<>();
        for (int i = 0; i < lst.size(); i++) {
            int pos = -1, pos2 = -1;
            for (int j = 0; j < lst.get(i).size(); j++) {
                if (lst.get(i).get(j) == x) {
                    pos = i;
                    pos2 = j;
                    break;
                }
            }
            if (pos > -1 && pos2 > -1) {
                res.add(new ArrayList<>());
                res.get(res.size() - 1).add(pos);
                res.get(res.size() - 1).add(pos2);
            }
        }
        res.sort((o1, o2) -> o1.get(0) == o2.get(0) ? o2.get(1) - o1.get(1) : o1.get(0) - o2.get(0));
        return res;
    }
}
