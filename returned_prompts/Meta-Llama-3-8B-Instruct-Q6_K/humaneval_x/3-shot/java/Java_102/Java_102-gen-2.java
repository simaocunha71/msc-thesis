        if (x % 2 == 0) {
            return y;
        } else if (y % 2 == 0) {
            return y;
        } else if (x > y) {
            return -1;
        } else {
            for (int i = x; i <= y; i++) {
                if (i % 2 == 0) {
                    return i;
                }
            }
            return -1;
        }
    }
}

