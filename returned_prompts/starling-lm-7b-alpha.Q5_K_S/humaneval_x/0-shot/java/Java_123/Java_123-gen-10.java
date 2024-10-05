        List<Integer> l = new ArrayList<Integer>();
        l.add(n);
        while (n != 1) {
            if (n % 2 == 1) {
                l.add(3 * n + 1);
                n = 3 * n + 1;
                continue A;
            } else {
                l.add(n / 2);
                n = n / 2;
                continue A;
            }
        }

        List<Integer> res = new ArrayList<Integer>();
        for (int i : l) {
            if (i % 2 == 1) {
                res.add(i);
            }
        }
        return res;
    }

    public static void main(String[] args) {
        Solution s = new Solution();
        System.out.println(s.getOddCollatz(5));
        System.out.println(s.getOddCollatz(6));
        System.out.println(s.getOddCollatz(7));
        System.out.println(s.getOddCollatz(8));
        System.out.println(s.getOddCollatz(10));
    }
}



























































































































































































































