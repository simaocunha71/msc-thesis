        if (x % 2 == 1) {
            x -= 1;
        }
        if (y % 2 == 1) {
            y -= 1;
        }
        if (x > y) {
            return -1;
        } else {
            return y;
        }
    }
}

