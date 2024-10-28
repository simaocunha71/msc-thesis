    public double median(List<Integer> l) {
        Collections.sort(l);
        int n = l.size();
        if (n % 2 == 1) {
            return (double) l.get(n / 2);
        } else {
            return (double) (l.get(n / 2 - 1) + l.get(n / 2)) / 2;
        }
    }