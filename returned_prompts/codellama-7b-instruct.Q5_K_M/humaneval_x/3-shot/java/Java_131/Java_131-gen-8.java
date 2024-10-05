        int result = 1;
        while (n > 0) {
            if (n % 10 == 1 || n % 10 == 3 || n % 10 == 5 || n % 10 == 7 || n % 10 == 9) {
                result *= n % 10;
            }
            n /= 10;
        }
        return result;
    }
}

