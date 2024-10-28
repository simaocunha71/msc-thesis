    public boolean monotonic(List<Integer> l) {
        int inc = Integer.MIN_VALUE;
        int dec = Integer.MAX_VALUE;
        for (int i = 0; i < l.size() - 1; i++) {
            if (l.get(i) <= l.get(i + 1)) {
                inc = Math.max(inc, l.get(i));
            } else {
                dec = Math.min(dec, l.get(i));
            }
        }
        return inc == Integer.MIN_VALUE || dec == Integer.MAX_VALUE || l.get(l.size() - 1) <= inc || l.get(0) >= dec;
    }