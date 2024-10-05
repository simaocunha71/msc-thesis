        if (lst.size() == 0 || lst.get(0).size() == 0) {
            return new ArrayList<List<Integer>>();
        }

        int rows = lst.size();
        int columns = lst.get(0).size();

        List<List<Integer>> result = new ArrayList<List<Integer>>();

        // step 1:
        // find coordinates of x in each row
        for (int i = 0; i < rows; i++) {
            int[] loc = locate(lst.get(i), x);
            if (loc[0] != -1) {
                result.add(new ArrayList<Integer>(Arrays.asList(i, loc[0])));
            }
        }

        // step 2:
        // sort coordinates by rows in ascending order
        Collections.sort(result, new Comparator<List<Integer>>() {
            @Override
            public int compare(List<Integer> a, List<Integer> b) {
                int r1 = a.get(0);
                int r2 = b.get(0);
                if (r1 < r2) {
                    return -1;
                } else if (r1 > r2) {
                    return 1;
                } else {
                    return 0;
                }
            }
        });

        // step 3:
        // sort coordinates by columns in descending order
        for (int i = 0; i < result.size(); i++) {
            int[] rc = result.get(i);
            int j = i + 1;
            while (j < result.size() && rc[0] == result.get(j)[0]) {
                int[] rc2 = result.get(j);
                if (rc2[1] < rc[1]) {
                    List<Integer> tmp = result.get(j);
                    result.set(j, result.get(i));
                    result.set(i, tmp);
                }
                j++;
            }
        }

        return result;
    }

    private int[] locate(List<Integer> lst,