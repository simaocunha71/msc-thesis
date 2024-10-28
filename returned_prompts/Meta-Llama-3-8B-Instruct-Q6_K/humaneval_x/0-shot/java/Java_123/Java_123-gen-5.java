    public List<Integer> getOddCollatz(int n) {
        List<Integer> res = new ArrayList<>();
        while(n != 1) {
            if(n % 2 == 0) {
                n = n / 2;
            } else {
                n = 3 * n + 1;
            }
            if(n % 2 != 0) {
                res.add(n);
            }
        }
        res.add(1);
        Collections.sort(res);
        return res;
    }