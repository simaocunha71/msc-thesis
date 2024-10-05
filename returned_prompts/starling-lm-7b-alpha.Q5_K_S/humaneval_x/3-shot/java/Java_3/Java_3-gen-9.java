        int balance = 0;
        for (int operation : operations) {
            if (balance + operation < 0) return true;
            balance += operation;
        }
        return false;
    }
}

