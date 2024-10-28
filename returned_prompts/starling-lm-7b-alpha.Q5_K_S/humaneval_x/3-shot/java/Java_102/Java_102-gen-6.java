        if (x % 2 != 0 && y % 2 != 0) {
            return -1;
        }
        if (x % 2 != 0 && y % 2 == 0) {
            return y;
        }
        if (x % 2 == 0 && y % 2 != 0) {
            return x;
        }
        if (x % 2 == 0 && y % 2 == 0) {
            return x;
        }
        return -1;
    }
}

