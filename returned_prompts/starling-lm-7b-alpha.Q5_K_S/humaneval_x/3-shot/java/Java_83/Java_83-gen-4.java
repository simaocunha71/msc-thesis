        if (n == 1) {
            return 2;
        }
        return (int) Math.pow(10, n) - (int) Math.pow(10, n - 1) + 10;
    }
}

