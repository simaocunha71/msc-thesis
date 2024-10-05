    public double median(List<Integer> l) {
        Collections.sort(l);
        int n = l.size();
        if (n % 2 == 0) {
            int mid1 = l.get(n / 2 - 1);
            int mid2 = l.get(n / 2);
            return ((double) (mid1 + mid2)) / 2;
        } else {
            return (double) l.get(n / 2);
        }
    }
}
