        int current_balance = 0;

        for (int amount : operations) {
            current_balance += amount;

            if (current_balance < 0) return true;
        }
        return false;
    }
}

