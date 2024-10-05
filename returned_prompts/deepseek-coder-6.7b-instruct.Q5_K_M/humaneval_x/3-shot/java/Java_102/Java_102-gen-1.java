        if (y % 2 == 0) {
            return y;
        } else if (x % 2 == 0) {
            return x;
        } else if ((y - x) >= 2) {
            return y - 1;
        } else {
            return -1;
        }
    }
}

