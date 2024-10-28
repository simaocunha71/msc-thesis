        List<Integer> result = new ArrayList<Integer>();
        for (int i = 2; i <= Math.sqrt(n); i++) {
            while (n % i == 0) {
                result.add(i);
                n = n / i;
            }
        }
        if (n > 1) {
            result.add(n);
        }
        return result;
    }

    public static void main(String[] args) {
        int n = 120;
        Solution s = new Solution();
        List<Integer> res = s.factorize(n);
        System.out.println(res);
    }
}
