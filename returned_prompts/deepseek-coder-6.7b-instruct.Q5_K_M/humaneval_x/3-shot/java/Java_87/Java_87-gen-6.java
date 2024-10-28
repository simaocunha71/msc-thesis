        List<List<Integer>> res = new ArrayList<>();
        for(int i = 0; i < lst.size(); i++) {
            for(int j = 0; j < lst.get(i).size(); j++) {
                if(lst.get(i).get(j) == x) {
                    res.add(Arrays.asList(i, j));
                }
            }
        }
        res.sort(Comparator.comparing((List<Integer> p) -> p.get(0)).thenComparing(p -> p.get(1), Comparator.reverseOrder()));
        return res;
    }
}

