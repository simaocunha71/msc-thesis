    public boolean belowZero(List<Integer> operations) {
        int balance = 0;
        for (int operation : operations) {
            balance += operation;
            if (balance < 0) {
                return true;
            }
        }
        return false;
    }  // Time complexity O(n) where n is the number of operations. Space complexity O(1) as it only uses a constant amount of space. 





