        int balance = 0;
        for (int i : operations) {
            balance += i;
            if (balance < 0) return true;
        }
        return false;
    }
}

