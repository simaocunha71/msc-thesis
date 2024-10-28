        List<List<Integer>> res = new ArrayList<List<Integer>>();
        for (int i = 0; i < lst.size(); i++) {
            int[] y = getY(lst.get(i), x);
            if (y[0] != -1)
                res.add(Arrays.asList(i, y[0]));
        }
        res.sort((a, b) -> {
            int r1 = a.get(0), r2 = b.get(0);
            int c1 = a.get(1), c2 = b.get(1);
            if (r1 < r2) return -1;
            else if (r1 > r2) return 1;
            else if (c1 > c2) return -1;
            else if (c1 < c2) return 1;
            else return 0;
        });
        return res;
    }

    public int[] getY(List<Integer> lst, int x) {
        int[] res = new int[1];
        res[0] = -1;
        int[] tmp = new int[1];
        tmp[0] = -1;
        for (int i = 0; i < lst.size(); i++) {
            if (lst.get(i) == x) {
                res[0] = i;
                break;
            }
        }
        if (res[0] != -1) {
            for (int i = res[0]; i < lst.size(); i++) {
                if (lst.get(i) != x) {
                    tmp[0] = i;
                    break;
                }
            }
        }
        if (res[0] == -1 || tmp[0] == -1) return res;
        return tmp;
    }

    public static void main(String[] args) {
        List<List<Integer>> lst = new ArrayList<List<Integer>>();
        lst.add(Arrays.asList(1, 2, 3, 4, 5, 6));
        lst.add(Arrays.asList(1, 2, 3