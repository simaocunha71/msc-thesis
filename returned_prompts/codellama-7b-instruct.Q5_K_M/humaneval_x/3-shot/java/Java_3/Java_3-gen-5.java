        int balance = 0;
        for (Integer operation : operations) {
            if (balance < 0) return true;
            balance += operation;
        }
        return false;
    }
}

