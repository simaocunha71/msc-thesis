        int sum = 0;
        while (a != 0 && b != 0) {
            sum = (sum + a % 10 * b % 10) % 10;
            a /= 10;
            b /= 10;
        }
        return sum;
    }

    public static void main(String[] args) {
        Solution s = new Solution();
        System.out.println(s.multiply(148, 412));
    }
}