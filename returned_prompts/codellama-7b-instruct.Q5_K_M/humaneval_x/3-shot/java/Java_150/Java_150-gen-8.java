        if (n == 2 || n == 3 || n == 5 || n == 7) return true;

        for (int i = 2; i < n / 2 + 1; i++) {
            if (n % i == 0) return false;
        }
        return true;
    }

}

