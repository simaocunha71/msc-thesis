    public double median(List<Integer> l) {
        Collections.sort(l);
        int n = l.size();
        if (n % 2 == 0) {
            int mid = n / 2;
            return (l.get(mid - 1) + l.get(mid)) / 2.0;
        } else {
            return (double) l.get(n / 2);
        }
    }
}

