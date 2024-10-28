        int balance = 0;
        for (int amount : operations) {
            balance += amount;
            if (balance < 0) return true;
        }
        return false;
    }
}

