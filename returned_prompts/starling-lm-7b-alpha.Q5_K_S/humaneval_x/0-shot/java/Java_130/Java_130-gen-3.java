        List<Integer> res = new ArrayList<>();
        if(n == 0) {
            return res;
        }
        res.add(3);
        if(n == 1) {
            return res;
        }
        res.add(1);
        if(n == 2) {
            return res;
        }
        res.add(2);
        for(int i = 3; i <= n; i++) {
            if(i % 2 == 0) {
                res.add(res.get(i - 1));
            }
            else {
                int prev1 = res.get(i - 1);
                int prev2 = res.get(i - 2);
                int prev3 = res.get(i + 1);
                int tmp = prev1 + prev2 + prev3;
                res.add(tmp);
            }
        }
        return res;
    }

    public static void main(String[] args) {
        Solution solution = new Solution();
        Scanner in = new Scanner(System.in);
        int n = in.nextInt();
        System.out.println(solution.tri(n));
    }
}



























































































































































































































