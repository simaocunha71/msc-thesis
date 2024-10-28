        if (n == 1) {
            if (x == 1) {
                return true;
            } else {
                return false;
            }
        }
        if (x == 0) {
            return false;
        }
        if (x < 0) {
            return false;
        }
        if (x == 1) {
            return true;
        }
        int i = 1;
        while (i <= x) {
            if (n == 2) {
                if (i % 2 == 1) {
                    i = i * 2;
                } else {
                    i = i / 2;
                }
            } else {
                i = i * n;
            }
            if (i == x) {
                break A;
            }
        }
        if (i == x) {
            return true;
        } else {
            return false;
        }
    }
}


















































































































































































































































































