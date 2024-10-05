        if (x % 2 == 0) {
            return y;
        } else if (y % 2 == 0) {
            return y;
        } else {
            if (x < y) {
                return y;
            } else {
                return -1;
            }
        }
    }
}

