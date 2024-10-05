        int result = 1;
        int last = 0;
        while (n > 0) {
            int d = n % 10;
            if (d % 2 != 0) {
                result *= d;
            }
            n /= 10;
        }
        return result;
    }
}

