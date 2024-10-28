        if (x > y) {
            return -1;
        } else if (x % 2 == 0 && y % 2 == 0) {
            return y;
        } else if (x % 2 == 1 && y % 2 == 1) {
            return y - 1;
        } else {
            return x;
        }
    }
}

