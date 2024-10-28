        for (int i = n / 2; i > 1; i -= 1) {
            if (n % i == 0) return i;
        }
        return 1;
    }
}

