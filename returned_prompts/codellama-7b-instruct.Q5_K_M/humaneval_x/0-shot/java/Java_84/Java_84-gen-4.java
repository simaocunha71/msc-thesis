        if (N < 0) return "0";
        if (N < 2) return Integer.toString(N);
        if (N == 2) return "10";

        int sum = 0;
        while (N > 0) {
            int digit = N % 2;
            if (digit > 0) sum += digit;
            N /= 2;
        }

        return Integer.toString(sum);
    }
}
