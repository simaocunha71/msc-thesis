        int ret = -1, freq = 0;
        for (int i : lst) {
            if (i > 0) {
                int cnt = 1;
                for (int j = i + 1; j < lst.size(); j++) {
                    if (lst.get(j) == i) {
                        cnt++;
                    }
                }
                if (cnt >= i && i > freq) {
                    ret = i;
                    freq = cnt;
                }
            }
        }
        return ret;
    }
}
