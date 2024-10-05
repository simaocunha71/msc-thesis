        int i = 0;
        int j = lst.size() - 1;
        int m = (i + j) / 2;
        int count = 0;
        int max = -1;
        while (i <= j) {
            if (lst.get(m) == i) {
                count = 0;
                for (int k = m; k < lst.size(); k++) {
                    if (lst.get(k) == lst.get(m)) {
                        count++;
                    } else {
                        break;
                    }
                }
                if (count >= lst.get(m)) {
                    max = Math.max(max, lst.get(m));
                }
            } else if (lst.get(m) < i) {
                i = m + 1;
            } else {
                j = m - 1;
            }
            m = (i + j) / 2;
        }
        return max;
    }
}
