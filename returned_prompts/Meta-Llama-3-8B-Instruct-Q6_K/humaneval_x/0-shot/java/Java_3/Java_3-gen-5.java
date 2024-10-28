    public boolean belowZero(List<Integer> operations) {
        int balance = 0;
        for (Integer operation : operations) {
            balance += operation;
            if (balance < 0) {
                return true;
            }
        }
        return false;
    }
}