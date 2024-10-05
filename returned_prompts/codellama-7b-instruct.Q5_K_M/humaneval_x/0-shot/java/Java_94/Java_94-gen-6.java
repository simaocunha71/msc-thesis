    public int skjkasdkd(List<Integer> lst) {
        int max = 0;
        for (int i : lst) {
            if (i > max) {
                max = i;
            }
        }
        return findMax(lst, max);
    }

    private int findMax(List<Integer> lst, int max) {
        if (lst.size() == 0) {
            return 0;
        }
        if (lst.get(0) > max) {
            max = lst.get(0);
        }
        return max;
    }

B:
    public int skjkasdkd(List<Integer> lst) {
        int max = 0;
        for (int i : lst) {
            if (i > max) {
                max = i;
            }
        }
        return findMax(lst, max);
    }

    private int findMax(List<Integer> lst, int max) {
        if (lst.size() == 0) {
            return 0;
        }
        if (lst.get(0) > max) {
            max = lst.get(0);
        }
        return max;
    }
}


