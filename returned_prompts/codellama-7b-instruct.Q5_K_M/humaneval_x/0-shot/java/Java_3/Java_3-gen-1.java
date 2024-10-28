        int balance = 0;
        for (int operation : operations) {
            balance += operation;
            if (balance < 0) {
                return true;
            }
        }
        return false;
    }

    public static void main(String[] args) {
        Solution solution = new Solution();
        System.out.println(solution.belowZero(Arrays.asList(1, 2, 3)));
        System.out.println(solution.belowZero(Arrays.asList(1, 2, -4, 5)));
    }
}
