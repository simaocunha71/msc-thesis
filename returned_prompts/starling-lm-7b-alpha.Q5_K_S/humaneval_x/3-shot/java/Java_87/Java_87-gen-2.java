        List<List<Integer>> result = new ArrayList<>();
        for (int i = 0; i < lst.size(); i++) {
            int index = lst.get(i).indexOf(x);
            if (index != -1) {
                result.add(Arrays.asList(i, index));
            }
        }
        Collections.sort(result, new Comparator<List<Integer>>() {
            @Override
            public int compare(List<Integer> l1, List<Integer> l2) {
                if (l1.get(0) == l2.get(0)) {
                    return -Integer.compare(l2.get(1), l1.get(1));
                }
                return Integer.compare(l1.get(0), l2.get(0));
            }
        });
        return result;
    }
}


```