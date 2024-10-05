        if (x > y) {
            int temp = x;
            x = y;
            y = temp;
        }
        while (y > 0 && y % 2 == 0) {
            y = y / 2;
        }
        if (y >= x) {
            return y;
        } else {
            return -1;
        }
    }
}


