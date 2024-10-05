        List<List<Integer>> res = new ArrayList<>();
        for (List<Integer> l : lst) {
            int index = Collections.binarySearch(l, x);
            if (index < 0) {
                index = -index - 1;
            }
            if (index < l.size()) {
                List<Integer> tmp = new ArrayList<>();
                tmp.add(Collections.binarySearch(lst, l));
                tmp.add(index);
                res.add(tmp);
            }
        }
        Collections.sort(res, new Comparator<List<Integer>>() {
            @Override
            public int compare(List<Integer> l1, List<Integer> l2) {
                return Integer.compare(l1.get(0), l2.get(0));
            }
        });
        Collections.sort(res.get(0), new Comparator<Integer>() {
            @Override
            public int compare(Integer i1, Integer i2) {
                return Integer.compare(i2, i1);
            }
        });
        for (int i = 1; i < res.size(); i++) {
            Collections.sort(res.get(i), new Comparator<Integer>() {
                @Override
                public int compare(Integer i1, Integer i2) {
                    return Integer.compare(i2, i1);
                }
            });
        }
        return res;
    }
}


































































































































































