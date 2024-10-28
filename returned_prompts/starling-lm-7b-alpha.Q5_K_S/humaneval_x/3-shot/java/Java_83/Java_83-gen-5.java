        if (n == 0) return 1;
        if (n == 1) return 2;
        return 10 * Math.pow(10, n - 1) + 9 * Math.pow(10, n - 2);
    }
}

