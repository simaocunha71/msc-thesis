        int b = 2;
        int c = 3;
        int d = 5;
        while (a > 1) {
            if (a % b == 0) {
                a = a / b;
                b = 2;
                c = 3;
                d = 5;
            } else if (a % c == 0) {
                a = a / c;
                c = 3;
                d = 5;
            } else if (a % d == 0) {
                a = a / d;
                return true;
            } else {
                return false;
            }
        }
        return false;
    }
}

