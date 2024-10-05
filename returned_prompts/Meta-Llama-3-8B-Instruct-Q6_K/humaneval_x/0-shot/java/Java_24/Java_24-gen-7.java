        int i = n;

        while (i > 1) {
            if (n % i == 0) {
                return i;
            }
            i--;
        }

        return 1;
    }
}
