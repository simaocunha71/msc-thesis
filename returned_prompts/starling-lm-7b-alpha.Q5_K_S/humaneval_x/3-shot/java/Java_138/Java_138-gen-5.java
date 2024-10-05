        if (n < 0) {
            return false;
        }
        if (n % 2 == 1) {
            return false;
        }
        if (n < 8) {
            return false;
        }
        if (n == 8) {
            return true;
        }
        if (n == 12) {
            return true;
        }
        if (n == 16) {
            return true;
        }
        if (n == 20) {
            return true;
        }
        return false;
    }
}


