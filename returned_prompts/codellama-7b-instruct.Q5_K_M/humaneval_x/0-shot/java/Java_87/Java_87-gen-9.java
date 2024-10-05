        List<List<Integer>> result = new ArrayList<>();

        for (int i = 0; i < lst.size(); i++) {

            List<Integer> row = lst.get(i);
            int[] indexes = new int[row.size()];
            int count = 0;

            for (int j = 0; j < row.size(); j++) {
                if (row.get(j) == x) {
                    indexes[count++] = j;
                }
            }

            Arrays.sort(indexes, 0, count);

            for (int k = 0; k < count; k++) {

                result.add(new ArrayList<>(Arrays.asList(i, indexes[k])));
            }
        }

        Collections.sort(result, new Comparator<List<Integer>>() {

            @Override
            public int compare(List<Integer> l1, List<Integer> l2) {
                if (l1.get(0) == l2.get(0)) {
                    return l2.get(1) - l1.get(1);
                }

                return l1.get(0) - l2.get(0);
            }
        });

        return result;
    }
}
