        if (n <= 1) return n;

        int prev = 0, next = 1;

        for (int i = 2; i <= n; i++) {
            int sum = prev + next;
            prev = next;
            next = sum;
        }

        return next;
     }
}

