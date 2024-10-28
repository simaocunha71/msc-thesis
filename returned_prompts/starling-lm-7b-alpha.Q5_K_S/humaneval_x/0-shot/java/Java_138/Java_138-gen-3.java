        if (n < 0) {
            return false;
        }

        if (n == 0) {
            return false;
        }

        if (n % 2 != 0) {
            return false;
        }

        if (n == 4) {
            return true;
        }

        if (n == 8) {
            return true;
        }

        if (n == 12) {
            return true;
        }

        if (n == 16) {
            return true;
        }

        boolean result = false;
        for (int i = 4; i <= n - 4; i += 2) {
            if (isEqualToSumEven(n - i)) {
                result = true;
                break A;
            }
        }

        return result;
    }

    public static void main(String[] args) {
        Solution sol = new Solution();
        System.out.println(sol.isEqualToSumEven(8));
    }
}



































































































































































































































































