        int sumOfSquares = 0;
        for (Object number : lst) {
            if (number instanceof Integer) {
                int n = (Integer) number;
                if (n >= 0 && n % 2 == 1) {
                    sumOfSquares += n * n;
                }
            }
        }
        return sumOfSquares;
    }
}

