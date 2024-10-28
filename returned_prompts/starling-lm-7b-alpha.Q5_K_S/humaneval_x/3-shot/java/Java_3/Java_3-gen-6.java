        int balance = 0;
        for (int operation : operations) {
            if (operation > 0) {
                balance += operation;
            } else {
                balance += operation;
                if (balance < 0) return true;
            }
        }
        return false;
    }
}

