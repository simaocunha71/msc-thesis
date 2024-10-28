        int result = 1;
        while (n > 0) {
            int r = n % 10;
            if (r % 2 != 0) result *= r;
            n /= 10;
        }
        return result;
    }
}

