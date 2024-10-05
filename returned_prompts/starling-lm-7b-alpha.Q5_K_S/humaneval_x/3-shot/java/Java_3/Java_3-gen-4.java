        int balance = 0;
        for (int op : operations) {
            if (op > 0) {
                balance += op;
            } else {
                balance += op;
                if (balance < 0) {
                    return true;
                }
            }
        }
        return false;
    }
}

