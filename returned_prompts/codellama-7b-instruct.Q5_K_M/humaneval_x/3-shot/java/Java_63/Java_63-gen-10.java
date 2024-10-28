        if (n == 0) return 0;
        if (n == 1) return 0;
        if (n == 2) return 1;

        int previous_previous = 0;
        int previous = 0;
        int current = 1;

        for (int i = 3; i <= n; i++) {
            int temp = current;
            current = previous + previous_previous + current;
            previous_previous = previous;
            previous = temp;
        }
        return current;
    }
}

