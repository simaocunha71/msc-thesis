        for (int i = 2; i <= x; i++) {
            if ((int) Math.pow(i, n) == x) {
                return true;
            }
        }
        return false;
    }
}

