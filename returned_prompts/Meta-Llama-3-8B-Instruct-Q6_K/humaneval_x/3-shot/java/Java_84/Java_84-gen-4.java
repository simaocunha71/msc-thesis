        int sum = 0;
        StringBuilder result = new StringBuilder();

        while (N > 0) {
            int remainder = N % 2;
            sum += remainder;
            result.append(remainder);
            N = N / 2;
        }
        return result.toString();
    }
}

