        if (n == 1) return 2;
        return (int) Math.pow(10, n) - 9 + 1 + 9 * (Math.pow(10, n - 1) - Math.pow(10, n - 2));
    }
}

