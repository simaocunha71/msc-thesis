        for (int i = n; i > 1; i--) {
            if (n % i == 0) {
                return i;
            }
        }
        return 1;
    }

    public static void main(String[] args) {
        Solution s = new Solution();
        System.out.println(s.largestDivisor(15));
        System.out.println(s.largestDivisor(17));
    }
}

