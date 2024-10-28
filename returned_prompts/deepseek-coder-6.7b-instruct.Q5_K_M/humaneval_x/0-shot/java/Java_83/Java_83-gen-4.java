        int count = 0;

        if(n == 1) {
            return 1;
        } else {
            count = 2 * (n - 1);
        }

        return count;
    }

    public static void main(String[] args) {
        Solution sol = new Solution();
        System.out.println(sol.startsOneEnds(1)); // should print 1
        System.out.println