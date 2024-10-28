        if (n <= 0) return false;
        for (int i = 2; i <= n; i += 2) {
            if (n - i < 0) return false;
            if (n - i == 0) return true;
        }
        return false;
    }

    public boolean isEqualToSumEven2(int n) {
        // write your code here
        for (int i = 2; i <= n; i += 2) {
            if (n - i < 0) return false;
            if (n - i == 0) return true;
        }
        return false;
    }

    public static void main(String[] args) {
        Solution s = new Solution();
        System.out.println(s.isEqualToSumEven2(12));
    }
}
