    public double median(List<Integer> l) {
        Collections.sort(l);
        int n = l.size();
        if (n % 2 == 0) {
            double median = (l.get(n / 2 - 1) + l.get(n / 2)) / 2.0;
            return median;
        } else {
            return (double) l.get(n / 2);
        }
    }
