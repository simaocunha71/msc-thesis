        if (x % 2 == 0) {
            if (x <= y) {
                return x;
            } else if (y % 2 == 0) {
                return y;
            } else {
                return y - 1;
            }
        } else {
            return -1;
        }
    }
}

