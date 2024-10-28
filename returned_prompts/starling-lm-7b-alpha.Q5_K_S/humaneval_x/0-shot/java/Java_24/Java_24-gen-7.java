        for (int i = n >> 1; i > 0; i--) {
            if (n % i == 0) {
                return i;
            }
        }
        return 1;
    }

    public static void main(String[] args) {
        Solution sol = new Solution();
        System.out.println(sol.largestDivisor(15));
    }
}




```