        int x = 0;
        int y = 0;
        int result = 0;
        while (a != 0) {
            if (a % 10 != 0) {
                x++;
            }
            a /= 10;
        }
        while (b != 0) {
            if (b % 10 != 0) {
                y++;
            }
            b /= 10;
        }
        a = x;
        b = y;
        while (a != 0 && b != 0) {
            if (a == 1 || b == 1) {
                result++;
            }
            a--;
            b--;
        }
        return result;
    }
}
